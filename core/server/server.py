import traceback
from pathlib import Path
from typing import AsyncGenerator, Any

import grpc
from grpc import Server, ServicerContext

import nonebot
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot
from core.rpc import hola_pb2_grpc, hola_pb2
from core.lib.async_queue import AsyncQueue
from core.lib.async_map import AsyncMap
from core.lib.event import event_parser


class Channel(hola_pb2_grpc.ChannelServicer):
    def __init__(self, server: Server, bot: Bot):
        self.server = server
        self.bot = bot
        self.request_queue = AsyncQueue("request")
        self.result_map = AsyncMap("result")

    async def option(
            self,
            request: hola_pb2.OptionCode,
            context: ServicerContext
    ) -> hola_pb2.OptionCode:
        if request.code == 1:
            await self.server.stop(0)

        return hola_pb2.OptionCode(code=request.code)

    async def match(
            self,
            event: hola_pb2.Event,
            context: ServicerContext
    ) -> hola_pb2.Empty:
        try:
            await self.bot.handle_event(event.plugins, await event_parser(event))
            return hola_pb2.Empty()

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())

    async def request(
            self,
            empty: hola_pb2.Empty,
            context: ServicerContext
    ) -> AsyncGenerator[hola_pb2.Request, Any]:
        logger.success("成功建立request连接")
        try:
            async for request in self.request_queue:
                yield hola_pb2.Request(**request)
        except StopAsyncIteration:
            logger.warning("中断request连接")
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())

    async def result(
            self,
            result_iterator: AsyncGenerator[hola_pb2.Result, Any],
            context
    ) -> hola_pb2.Empty:
        logger.success("成功建立result连接")
        try:
            async for result in result_iterator:
                await self.result_map.set(result.request_id, result)
        except StopAsyncIteration:
            logger.warning("中断result连接")
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
        finally:
            return hola_pb2.Empty()


def create_server(host, port):
    server: Server = grpc.aio.server(
        options=[
            ('grpc.max_send_message_length', 256 * 1024 * 1024),
            ('grpc.max_receive_message_length', 256 * 1024 * 1024),
        ]
    )
    server.add_insecure_port(f'{host or "127.0.0.1"}:{port or 50052}')
    hola_pb2_grpc.add_ChannelServicer_to_server(Channel(server, nonebot.get_bot()), server)
    return server
