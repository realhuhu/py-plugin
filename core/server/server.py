import json
import traceback
from concurrent import futures

import grpc

from core.rpc import type_pb2_grpc, type_pb2
from core.lib.exception import *


class Servicer(type_pb2_grpc.ChannelServicer):
    def __init__(self, apps, server):
        self.apps = dict(apps)
        self.server = server

    def UnaryToUnary(self, request, context):
        try:
            if not request.file or not request.function:
                raise Exception("no file or function")

            handler = getattr(self.apps.get(request.file), request.function, None)

            if not handler:
                raise Exception("no handler")

            channel_type = getattr(handler, "__channel_type__", None)

            if channel_type != "UnaryToUnary":
                raise Exception(f"wrong handler, expect UnaryToUnary function, got {channel_type}")

            return type_pb2.Response(**handler(request))

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(traceback.format_exc())

    def StreamToUnary(self, request_iterator, context):
        try:
            try:
                head = request_iterator.next()
            except Exception:
                raise StreamInitException(traceback.format_exc())

            if not head.file or not head.function:
                raise Exception("no file or function")

            handler = getattr(self.apps.get(head.file), head.function, None)

            if not handler:
                raise Exception("no handler")

            channel_type = getattr(handler, "__channel_type__", None)

            if channel_type != "StreamToUnary":
                raise Exception(f"wrong handler, expect StreamToUnary, got {channel_type}")

            return type_pb2.Response(**handler(request_iterator))

        except StreamInitException as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(e.stack)

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(traceback.format_exc())

    def UnaryToStream(self, request, context):
        try:
            if not request.file or not request.function:
                raise Exception("no file or function")

            handler = getattr(self.apps.get(request.file), request.function, None)

            if not handler:
                raise Exception("no handler")

            channel_type = getattr(handler, "__channel_type__", None)

            if channel_type != "UnaryToStream":
                raise Exception(f"wrong handler, expect UnaryToStream, got {channel_type}")

            for response in handler(request):
                yield type_pb2.Response(**response)

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(traceback.format_exc())

    def StreamToStream(self, request_iterator, context):
        try:
            try:
                head = request_iterator.next()
            except Exception:
                raise StreamInitException(traceback.format_exc())

            if not head.file or not head.function:
                raise Exception("no file or function")

            handler = getattr(self.apps.get(head.file), head.function, None)

            if not handler:
                raise Exception("no handler")

            channel_type = getattr(handler, "__channel_type__", None)

            if channel_type != "StreamToStream":
                raise Exception(f"wrong handler, expect StreamToStream, got {channel_type}")

            for response in handler(request_iterator):
                yield type_pb2.Response(**response)

        except StreamInitException as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(e.stack)

        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            raise context.set_details(traceback.format_exc())

    def Option(self, request, context):
        if request.code == 1:
            self.server.stop(0)
            self.server = None
        return type_pb2.ResponseCode(code=request.code)


def startServer(path, apps):
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = Servicer(apps, server)
    type_pb2_grpc.add_ChannelServicer_to_server(servicer, server)
    server.add_insecure_port(f'{config.get("host", "127.0.0.1")}:{config.get("port", 50051)}')
    server.start()
    return server
