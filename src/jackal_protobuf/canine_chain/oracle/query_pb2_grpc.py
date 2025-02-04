# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from jackal_protobuf.canine_chain.oracle import query_pb2 as canine__chain_dot_oracle_dot_query__pb2

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
        + f' but the generated code in canine_chain/oracle/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/canine_chain.oracle.Query/Params',
                request_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryParams.SerializeToString,
                response_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.Feed = channel.unary_unary(
                '/canine_chain.oracle.Query/Feed',
                request_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryFeed.SerializeToString,
                response_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryFeedResponse.FromString,
                _registered_method=True)
        self.AllFeeds = channel.unary_unary(
                '/canine_chain.oracle.Query/AllFeeds',
                request_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryAllFeeds.SerializeToString,
                response_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryAllFeedsResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Feed(self, request, context):
        """Queries a Feed by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllFeeds(self, request, context):
        """Queries a list of Feed items.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryParams.FromString,
                    response_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'Feed': grpc.unary_unary_rpc_method_handler(
                    servicer.Feed,
                    request_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryFeed.FromString,
                    response_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryFeedResponse.SerializeToString,
            ),
            'AllFeeds': grpc.unary_unary_rpc_method_handler(
                    servicer.AllFeeds,
                    request_deserializer=canine__chain_dot_oracle_dot_query__pb2.QueryAllFeeds.FromString,
                    response_serializer=canine__chain_dot_oracle_dot_query__pb2.QueryAllFeedsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'canine_chain.oracle.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('canine_chain.oracle.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Params(request,
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
            '/canine_chain.oracle.Query/Params',
            canine__chain_dot_oracle_dot_query__pb2.QueryParams.SerializeToString,
            canine__chain_dot_oracle_dot_query__pb2.QueryParamsResponse.FromString,
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
    def Feed(request,
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
            '/canine_chain.oracle.Query/Feed',
            canine__chain_dot_oracle_dot_query__pb2.QueryFeed.SerializeToString,
            canine__chain_dot_oracle_dot_query__pb2.QueryFeedResponse.FromString,
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
    def AllFeeds(request,
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
            '/canine_chain.oracle.Query/AllFeeds',
            canine__chain_dot_oracle_dot_query__pb2.QueryAllFeeds.SerializeToString,
            canine__chain_dot_oracle_dot_query__pb2.QueryAllFeedsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
