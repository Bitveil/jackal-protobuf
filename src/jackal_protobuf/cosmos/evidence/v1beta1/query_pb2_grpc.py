
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.evidence.v1beta1 import query_pb2 as cosmos_dot_evidence_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Evidence = channel.unary_unary('/cosmos.evidence.v1beta1.Query/Evidence', request_serializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceRequest.SerializeToString, response_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceResponse.FromString)
        self.AllEvidence = channel.unary_unary('/cosmos.evidence.v1beta1.Query/AllEvidence', request_serializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceRequest.SerializeToString, response_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Evidence(self, request, context):
        'Evidence queries evidence based on evidence hash.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllEvidence(self, request, context):
        'AllEvidence queries all evidence.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Evidence': grpc.unary_unary_rpc_method_handler(servicer.Evidence, request_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceRequest.FromString, response_serializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceResponse.SerializeToString), 'AllEvidence': grpc.unary_unary_rpc_method_handler(servicer.AllEvidence, request_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceRequest.FromString, response_serializer=cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.evidence.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Evidence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.evidence.v1beta1.Query/Evidence', cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceRequest.SerializeToString, cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryEvidenceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllEvidence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.evidence.v1beta1.Query/AllEvidence', cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceRequest.SerializeToString, cosmos_dot_evidence_dot_v1beta1_dot_query__pb2.QueryAllEvidenceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
