# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from core.rpc import hola_pb2 as core_dot_rpc_dot_hola__pb2


class ChannelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.option = channel.unary_unary(
                '/hola.Channel/option',
                request_serializer=core_dot_rpc_dot_hola__pb2.OptionCode.SerializeToString,
                response_deserializer=core_dot_rpc_dot_hola__pb2.OptionCode.FromString,
                )
        self.match = channel.unary_unary(
                '/hola.Channel/match',
                request_serializer=core_dot_rpc_dot_hola__pb2.Event.SerializeToString,
                response_deserializer=core_dot_rpc_dot_hola__pb2.OptionCode.FromString,
                )
        self.callBack = channel.stream_stream(
                '/hola.Channel/callBack',
                request_serializer=core_dot_rpc_dot_hola__pb2.Result.SerializeToString,
                response_deserializer=core_dot_rpc_dot_hola__pb2.Request.FromString,
                )


class ChannelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def option(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def match(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def callBack(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChannelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'option': grpc.unary_unary_rpc_method_handler(
                    servicer.option,
                    request_deserializer=core_dot_rpc_dot_hola__pb2.OptionCode.FromString,
                    response_serializer=core_dot_rpc_dot_hola__pb2.OptionCode.SerializeToString,
            ),
            'match': grpc.unary_unary_rpc_method_handler(
                    servicer.match,
                    request_deserializer=core_dot_rpc_dot_hola__pb2.Event.FromString,
                    response_serializer=core_dot_rpc_dot_hola__pb2.OptionCode.SerializeToString,
            ),
            'callBack': grpc.stream_stream_rpc_method_handler(
                    servicer.callBack,
                    request_deserializer=core_dot_rpc_dot_hola__pb2.Result.FromString,
                    response_serializer=core_dot_rpc_dot_hola__pb2.Request.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hola.Channel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Channel(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def option(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hola.Channel/option',
            core_dot_rpc_dot_hola__pb2.OptionCode.SerializeToString,
            core_dot_rpc_dot_hola__pb2.OptionCode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def match(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hola.Channel/match',
            core_dot_rpc_dot_hola__pb2.Event.SerializeToString,
            core_dot_rpc_dot_hola__pb2.OptionCode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def callBack(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/hola.Channel/callBack',
            core_dot_rpc_dot_hola__pb2.Result.SerializeToString,
            core_dot_rpc_dot_hola__pb2.Request.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
