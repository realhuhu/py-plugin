import asyncio
import traceback
from collections import defaultdict
from typing import Dict, AsyncGenerator, Any

import grpc
from nonebot import logger
from nonebot.config import Config

from yunzai_nonebot.rpc import hola_pb2_grpc, hola_pb2
from yunzai_nonebot.utils import AsyncQueue
from yunzai_nonebot.utils.exception import InitChannelError


class Servicer(hola_pb2_grpc.Pipe):
    def __init__(self, handler, config: Config):
        self.connections: Dict[str, asyncio.Task] = {}
        self.contexts: Dict[str, grpc.ServicerContext] = {}
        self.handler = handler
        self.server: grpc.Server = grpc.aio.server(
            options=[
                ('grpc.max_send_message_length', 256 * 1024 * 1024),
                ('grpc.max_receive_message_length', 256 * 1024 * 1024),
            ]
        )
        hola_pb2_grpc.add_PipeServicer_to_server(self, self.server)
        self.server.add_insecure_port(f'{config.host}:{config.port}')

    async def Option(
            self,
            request: hola_pb2.OptionCode,
            context: grpc.ServicerContext,
            **kwargs
    ):
        code = request.code
        if code == 1:
            await self.server.stop(0)

        return hola_pb2.OptionCode(code=code)

    async def Channel(
            self,
            request_iterator: AsyncGenerator[hola_pb2.ToServer, Any],
            context: grpc.ServicerContext,
            **kwargs
    ) -> AsyncGenerator[hola_pb2.ToClient, Any]:
        try:
            init = await request_iterator.__anext__()

            if init.WhichOneof("to_server_type") != "head":
                raise InitChannelError

            self_id = init.head.self_id
            if context := self.contexts.get(self_id):
                context.abort_with_status(grpc.StatusCode.OK)

            self.connections[self_id] = asyncio.create_task(self.handler(self_id, request_iterator))
            logger.success(f"{init.head.self_id}已连接")
            async for response in AsyncQueue(self_id):
                logger.debug(f"发出请求:{response}")
                yield response
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
