# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from waves.node.grpc import accounts_api_pb2 as waves_dot_node_dot_grpc_dot_accounts__api__pb2


class AccountsApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalances = channel.unary_stream(
                '/waves.node.grpc.AccountsApi/GetBalances',
                request_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalancesRequest.SerializeToString,
                response_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalanceResponse.FromString,
                )
        self.GetScript = channel.unary_unary(
                '/waves.node.grpc.AccountsApi/GetScript',
                request_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.SerializeToString,
                response_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.ScriptData.FromString,
                )
        self.GetActiveLeases = channel.unary_stream(
                '/waves.node.grpc.AccountsApi/GetActiveLeases',
                request_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.SerializeToString,
                response_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.LeaseResponse.FromString,
                )
        self.GetDataEntries = channel.unary_stream(
                '/waves.node.grpc.AccountsApi/GetDataEntries',
                request_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataRequest.SerializeToString,
                response_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataEntryResponse.FromString,
                )
        self.ResolveAlias = channel.unary_unary(
                '/waves.node.grpc.AccountsApi/ResolveAlias',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
                )


class AccountsApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBalances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveLeases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResolveAlias(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountsApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalances': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBalances,
                    request_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalancesRequest.FromString,
                    response_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalanceResponse.SerializeToString,
            ),
            'GetScript': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScript,
                    request_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.FromString,
                    response_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.ScriptData.SerializeToString,
            ),
            'GetActiveLeases': grpc.unary_stream_rpc_method_handler(
                    servicer.GetActiveLeases,
                    request_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.FromString,
                    response_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.LeaseResponse.SerializeToString,
            ),
            'GetDataEntries': grpc.unary_stream_rpc_method_handler(
                    servicer.GetDataEntries,
                    request_deserializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataRequest.FromString,
                    response_serializer=waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataEntryResponse.SerializeToString,
            ),
            'ResolveAlias': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolveAlias,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'waves.node.grpc.AccountsApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountsApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBalances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/waves.node.grpc.AccountsApi/GetBalances',
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalancesRequest.SerializeToString,
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.BalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/waves.node.grpc.AccountsApi/GetScript',
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.SerializeToString,
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.ScriptData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveLeases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/waves.node.grpc.AccountsApi/GetActiveLeases',
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.AccountRequest.SerializeToString,
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.LeaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDataEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/waves.node.grpc.AccountsApi/GetDataEntries',
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataRequest.SerializeToString,
            waves_dot_node_dot_grpc_dot_accounts__api__pb2.DataEntryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResolveAlias(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/waves.node.grpc.AccountsApi/ResolveAlias',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
