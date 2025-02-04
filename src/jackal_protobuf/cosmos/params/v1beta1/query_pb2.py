
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.params.v1beta1 import params_pb2 as cosmos_dot_params_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/params/v1beta1/query.proto\x12\x15cosmos.params.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a"cosmos/params/v1beta1/params.proto"3\n\x12QueryParamsRequest\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"N\n\x13QueryParamsResponse\x127\n\x05param\x18\x01 \x01(\x0b2".cosmos.params.v1beta1.ParamChangeB\x04\xc8\xde\x1f\x002\x90\x01\n\x05Query\x12\x86\x01\n\x06Params\x12).cosmos.params.v1beta1.QueryParamsRequest\x1a*.cosmos.params.v1beta1.QueryParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/paramsB6Z4github.com/cosmos/cosmos-sdk/x/params/types/proposalb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.params.v1beta1.query_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal'
    _QUERYPARAMSRESPONSE.fields_by_name['param']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['param']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/params'
    _QUERYPARAMSREQUEST._serialized_start = 148
    _QUERYPARAMSREQUEST._serialized_end = 199
    _QUERYPARAMSRESPONSE._serialized_start = 201
    _QUERYPARAMSRESPONSE._serialized_end = 279
    _QUERY._serialized_start = 282
    _QUERY._serialized_end = 426
