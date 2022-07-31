import json
from concurrent import futures

import grpc

from core.rpc import type_pb2_grpc, type_pb2


class Servicer(type_pb2_grpc.ChannelServicer):
    def __init__(self, apps, server):
        self.apps = dict(apps)
        self.server = server

    def UnaryToUnary(self, request, context):
        if not request.file or not request.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.apps.get(request.file), request.function, None)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        channel_type = getattr(handler, "__channel_type__", None)

        if channel_type != "UnaryToUnary":
            return type_pb2.Response(
                message={"error": f"wrong handler, expect UnaryToUnary function, got {channel_type}"}
            )

        return type_pb2.Response(**handler(request))

    def StreamToUnary(self, request_iterator, context):
        head = request_iterator.next()

        if not head.file or not head.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.apps.get(head.file), head.function, None)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        channel_type = getattr(handler, "__channel_type__", None)

        if channel_type != "StreamToUnary":
            return type_pb2.Response(
                message={"error": f"wrong handler, expect StreamToUnary, got {channel_type}"}
            )

        return type_pb2.Response(**handler(request_iterator))

    def UnaryToStream(self, request, context):
        if not request.file or not request.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.apps.get(request.file), request.function, None)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        channel_type = getattr(handler, "__channel_type__", None)

        if channel_type != "UnaryToStream":
            return type_pb2.Response(
                message={"error": f"wrong handler, expect UnaryToStream, got {channel_type}"}
            )

        for response in handler(request):
            yield type_pb2.Response(**response)

    def StreamToStream(self, request_iterator, context):
        head = request_iterator.next()

        if not head.file or not head.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.apps.get(head.file), head.function, None)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        channel_type = getattr(handler, "__channel_type__", None)

        if channel_type != "StreamToStream":
            return type_pb2.Response(
                message={"error": f"wrong handler, expect StreamToStream, got {channel_type}"}
            )

        for response in handler(request_iterator):
            yield type_pb2.Response(**response)

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
    return server, servicer
