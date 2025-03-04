
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.feegrant.v1beta1 import query_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Allowance = channel.unary_unary('/cosmos.feegrant.v1beta1.Query/Allowance', request_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceRequest.SerializeToString, response_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceResponse.FromString)
        self.Allowances = channel.unary_unary('/cosmos.feegrant.v1beta1.Query/Allowances', request_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesRequest.SerializeToString, response_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Allowance(self, request, context):
        'Allowance returns fee granted to the grantee by the granter.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Allowances(self, request, context):
        'Allowances returns all the grants for address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Allowance': grpc.unary_unary_rpc_method_handler(servicer.Allowance, request_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceRequest.FromString, response_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceResponse.SerializeToString), 'Allowances': grpc.unary_unary_rpc_method_handler(servicer.Allowances, request_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesRequest.FromString, response_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.feegrant.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Allowance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.feegrant.v1beta1.Query/Allowance', cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceRequest.SerializeToString, cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowanceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Allowances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.feegrant.v1beta1.Query/Allowances', cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesRequest.SerializeToString, cosmos_dot_feegrant_dot_v1beta1_dot_query__pb2.QueryAllowancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
