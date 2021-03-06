# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from waves.events.grpc import blockchain_updates_pb2 as waves_dot_events_dot_grpc_dot_blockchain__updates__pb2


class BlockchainUpdatesApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBlockUpdate = channel.unary_unary(
                '/waves.events.grpc.BlockchainUpdatesApi/GetBlockUpdate',
                request_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateRequest.SerializeToString,
                response_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateResponse.FromString,
                )
        self.GetBlockUpdatesRange = channel.unary_unary(
                '/waves.events.grpc.BlockchainUpdatesApi/GetBlockUpdatesRange',
                request_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeRequest.SerializeToString,
                response_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/waves.events.grpc.BlockchainUpdatesApi/Subscribe',
                request_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeEvent.FromString,
                )


class BlockchainUpdatesApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBlockUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockUpdatesRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BlockchainUpdatesApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBlockUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockUpdate,
                    request_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateRequest.FromString,
                    response_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateResponse.SerializeToString,
            ),
            'GetBlockUpdatesRange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockUpdatesRange,
                    request_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeRequest.FromString,
                    response_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeRequest.FromString,
                    response_serializer=waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'waves.events.grpc.BlockchainUpdatesApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BlockchainUpdatesApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBlockUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/waves.events.grpc.BlockchainUpdatesApi/GetBlockUpdate',
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateRequest.SerializeToString,
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockUpdatesRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/waves.events.grpc.BlockchainUpdatesApi/GetBlockUpdatesRange',
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeRequest.SerializeToString,
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.GetBlockUpdatesRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/waves.events.grpc.BlockchainUpdatesApi/Subscribe',
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeRequest.SerializeToString,
            waves_dot_events_dot_grpc_dot_blockchain__updates__pb2.SubscribeEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
