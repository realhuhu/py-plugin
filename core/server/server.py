import json
from concurrent import futures

import grpc

from core.rpc import type_pb2_grpc, type_pb2


class Servicer(type_pb2_grpc.ChannelServicer):
    def __init__(self, apps, server):
        self.UnaryToUnaryApps = {}
        self.StreamToUnaryApps = {}
        self.UnaryToStreamApps = {}
        self.StreamToStreamApps = {}
        self.server = server
        for app in apps:
            name, module = app
            if not hasattr(module, "config") or not isinstance(module.config, dict):
                self.UnaryToUnaryApps[name] = module
            else:
                channel_type = module.config.get("type")
                if channel_type == "UnaryToUnary":
                    self.UnaryToUnaryApps[name] = module
                elif channel_type == "StreamToUnary":
                    self.StreamToUnaryApps[name] = module
                elif channel_type == "UnaryToStream":
                    self.UnaryToStreamApps[name] = module
                elif channel_type == "StreamToStream":
                    self.StreamToStreamApps[name] = module
                else:
                    self.UnaryToUnaryApps[name] = module

    def UnaryToUnary(self, request, context):
        if not request.file or not request.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.UnaryToUnaryApps.get(request.file), request.function)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        return type_pb2.Response(**handler(request))

    def StreamToUnary(self, request_iterator, context):
        try:
            head = request_iterator.next()
        except Exception:
            return type_pb2.Response()

        if not head.file or not head.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.StreamToUnaryApps.get(head.file), head.function)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        return type_pb2.Response(**handler(head, request_iterator))

    def UnaryToStream(self, request, context):
        if not request.file or not request.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.UnaryToStreamApps.get(request.file), request.function)

        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        for response in handler(request):
            yield type_pb2.Response(**response)

    def StreamToStream(self, request_iterator, context):
        try:
            head = request_iterator.next()
        except Exception:
            return type_pb2.Response()

        if not head.file or not head.function:
            return type_pb2.Response(message={"error": "no file or function"})

        handler = getattr(self.StreamToStreamApps.get(head.file), head.function)
        if not handler:
            return type_pb2.Response(message={"error": "no handler"})

        for response in handler(head, request_iterator):
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
