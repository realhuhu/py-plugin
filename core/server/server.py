import traceback
from typing import AsyncGenerator, Any

import grpc
from grpc import Server, ServicerContext

import nonebot
from nonebot.log import logger
from core.rpc import hola_pb2_grpc, hola_pb2
from core.lib.event import event_parser


class Channel(hola_pb2_grpc.ChannelServicer):
    def __init__(self, server: Server):
        self.server = server

    async def option(
            self,
            request: hola_pb2.OptionCode,
            context: ServicerContext
    ) -> hola_pb2.OptionCode:
        if hasattr(nonebot.get_driver().config, "server"):
            return hola_pb2.OptionCode(code=request.code)

        if request.code == 1:
            await self.server.stop(0)

        return hola_pb2.OptionCode(code=request.code)

    async def match(
            self,
            event: hola_pb2.Event,
            context: ServicerContext
    ) -> hola_pb2.Empty:
        try:
            await nonebot.get_bot(str(event.self_id)).handle_event(await event_parser(event), event.plugins)
            return hola_pb2.Empty()

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())

    async def request(
            self,
            head: hola_pb2.Head,
            context: ServicerContext
    ) -> AsyncGenerator[hola_pb2.Request, Any]:
        logger.success("成功建立request连接")
        bot = nonebot.get_bot(str(head.self_id))
        try:
            async for request in bot.request_queue:
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
        bot = nonebot.get_bot(str((await result_iterator.__anext__()).self_id))
        try:
            async for result in result_iterator:
                await bot.result_map.set(result.request_id, result)
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
    hola_pb2_grpc.add_ChannelServicer_to_server(Channel(server), server)
    return server
