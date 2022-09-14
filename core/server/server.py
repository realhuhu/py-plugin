import traceback

import grpc
from nonebot import logger
from core.rpc import type_pb2_grpc, type_pb2
from core.lib.exception import *
from core import config


class Servicer(type_pb2_grpc.ChannelServicer):
    def __init__(self, apps, server):
        self.apps = dict(apps)
        self.server = server
        logger.info(f"Plugins loaded:{' '.join(self.apps.keys())}")

    async def FrameToFrame(self, request, context):
        try:
            handler = self._get_handler(request, "FrameToFrame")

            return await handler(request)

        except Exception as e:
            if e.__class__ == RuntimeError and str(e) == "async generator raised StopAsyncIteration":
                pass
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(traceback.format_exc())

    async def StreamToFrame(self, request_iterator, context):
        try:
            try:
                head = await request_iterator.__anext__()
            except Exception:
                raise StreamInitException(traceback.format_exc())

            handler = self._get_handler(head, "StreamToFrame")

            return await handler(request_iterator)

        except StreamInitException as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(e.stack)

        except Exception as e:
            if e.__class__ == RuntimeError and str(e) == "async generator raised StopAsyncIteration":
                pass
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(traceback.format_exc())

    async def FrameToStream(self, request, context):
        try:
            handler = self._get_handler(request, "FrameToStream")
            async for response in handler(request):
                await context.write(response)

        except Exception as e:
            if e.__class__ == RuntimeError and str(e) == "async generator raised StopAsyncIteration":
                pass
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(traceback.format_exc())

    async def StreamToStream(self, request_iterator, context):
        try:
            try:
                head = await request_iterator.__anext__()
            except Exception:
                raise StreamInitException(traceback.format_exc())

            handler = self._get_handler(head, "StreamToStream")

            async for response in handler(request_iterator):
                await context.write(response)

        except StreamInitException as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(e.stack)

        except Exception as e:
            if e.__class__ == RuntimeError and str(e) == "async generator raised StopAsyncIteration":
                pass
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(traceback.format_exc())

    async def Option(self, request, context):
        if request.code == 1:
            await self.server.stop(0)

        return type_pb2.ResponseCode(code=request.code)

    def _get_handler(self, frame, handler_type):

        if not frame.package or not frame.handler:
            raise Exception("没有指定package或handler")

        package = self.apps.get(frame.package)

        if not package:
            raise Exception(f"package不存在:{frame.package}")

        handler = getattr(package, frame.handler, None)

        if not handler:
            raise Exception(f"package {frame.package}中没有该handler:{frame.handler}")

        __type__ = getattr(handler, "__type__", None)

        if __type__ != handler_type:
            raise Exception(f"您采用的是{handler_type}调用，但您指定的handler是{__type__}函数，调用失败")

        return handler


async def startServer(apps):
    server = grpc.aio.server(options=[
        ('grpc.max_send_message_length', 256 * 1024 * 1024),
        ('grpc.max_receive_message_length', 256 * 1024 * 1024),
    ])
    server.add_insecure_port(f'{config.grpc_host or "127.0.0.1"}:{config.grpc_port or 50051}')

    servicer = Servicer(apps, server)
    type_pb2_grpc.add_ChannelServicer_to_server(servicer, server)
    return server


__version__ = [1, 2, 0]
