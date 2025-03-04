# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from jackal_protobuf.canine_chain.filetree import query_pb2 as canine__chain_dot_filetree_dot_query__pb2

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
        + f' but the generated code in canine_chain/filetree/query_pb2_grpc.py depends on'
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
                '/canine_chain.filetree.Query/Params',
                request_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryParams.SerializeToString,
                response_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.File = channel.unary_unary(
                '/canine_chain.filetree.Query/File',
                request_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryFile.SerializeToString,
                response_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryFileResponse.FromString,
                _registered_method=True)
        self.AllFiles = channel.unary_unary(
                '/canine_chain.filetree.Query/AllFiles',
                request_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllFiles.SerializeToString,
                response_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllFilesResponse.FromString,
                _registered_method=True)
        self.PubKey = channel.unary_unary(
                '/canine_chain.filetree.Query/PubKey',
                request_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryPubKey.SerializeToString,
                response_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryPubKeyResponse.FromString,
                _registered_method=True)
        self.AllPubKeys = channel.unary_unary(
                '/canine_chain.filetree.Query/AllPubKeys',
                request_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeys.SerializeToString,
                response_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeysResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def File(self, request, context):
        """Queries a File by address and owner_address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllFiles(self, request, context):
        """Queries a list of File items.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PubKey(self, request, context):
        """Queries a PubKey by address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllPubKeys(self, request, context):
        """Queries a list of PubKey items.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryParams.FromString,
                    response_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'File': grpc.unary_unary_rpc_method_handler(
                    servicer.File,
                    request_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryFile.FromString,
                    response_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryFileResponse.SerializeToString,
            ),
            'AllFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.AllFiles,
                    request_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllFiles.FromString,
                    response_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllFilesResponse.SerializeToString,
            ),
            'PubKey': grpc.unary_unary_rpc_method_handler(
                    servicer.PubKey,
                    request_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryPubKey.FromString,
                    response_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryPubKeyResponse.SerializeToString,
            ),
            'AllPubKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.AllPubKeys,
                    request_deserializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeys.FromString,
                    response_serializer=canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeysResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'canine_chain.filetree.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('canine_chain.filetree.Query', rpc_method_handlers)


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
            '/canine_chain.filetree.Query/Params',
            canine__chain_dot_filetree_dot_query__pb2.QueryParams.SerializeToString,
            canine__chain_dot_filetree_dot_query__pb2.QueryParamsResponse.FromString,
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
    def File(request,
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
            '/canine_chain.filetree.Query/File',
            canine__chain_dot_filetree_dot_query__pb2.QueryFile.SerializeToString,
            canine__chain_dot_filetree_dot_query__pb2.QueryFileResponse.FromString,
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
    def AllFiles(request,
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
            '/canine_chain.filetree.Query/AllFiles',
            canine__chain_dot_filetree_dot_query__pb2.QueryAllFiles.SerializeToString,
            canine__chain_dot_filetree_dot_query__pb2.QueryAllFilesResponse.FromString,
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
    def PubKey(request,
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
            '/canine_chain.filetree.Query/PubKey',
            canine__chain_dot_filetree_dot_query__pb2.QueryPubKey.SerializeToString,
            canine__chain_dot_filetree_dot_query__pb2.QueryPubKeyResponse.FromString,
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
    def AllPubKeys(request,
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
            '/canine_chain.filetree.Query/AllPubKeys',
            canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeys.SerializeToString,
            canine__chain_dot_filetree_dot_query__pb2.QueryAllPubKeysResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
