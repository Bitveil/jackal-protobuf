# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from jackal_protobuf.canine_chain.oracle import tx_pb2 as canine__chain_dot_oracle_dot_tx__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in canine_chain/oracle/tx_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MsgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFeed = channel.unary_unary(
                '/canine_chain.oracle.Msg/CreateFeed',
                request_serializer=canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeed.SerializeToString,
                response_deserializer=canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeedResponse.FromString,
                _registered_method=True)
        self.UpdateFeed = channel.unary_unary(
                '/canine_chain.oracle.Msg/UpdateFeed',
                request_serializer=canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeed.SerializeToString,
                response_deserializer=canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeedResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFeed,
                    request_deserializer=canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeed.FromString,
                    response_serializer=canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeedResponse.SerializeToString,
            ),
            'UpdateFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFeed,
                    request_deserializer=canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeed.FromString,
                    response_serializer=canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'canine_chain.oracle.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('canine_chain.oracle.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/canine_chain.oracle.Msg/CreateFeed',
            canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeed.SerializeToString,
            canine__chain_dot_oracle_dot_tx__pb2.MsgCreateFeedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/canine_chain.oracle.Msg/UpdateFeed',
            canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeed.SerializeToString,
            canine__chain_dot_oracle_dot_tx__pb2.MsgUpdateFeedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
