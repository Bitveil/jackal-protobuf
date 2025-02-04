
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/crisis/v1beta1/tx.proto\x12\x15cosmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto"\xa4\x01\n\x12MsgVerifyInvariant\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12?\n\x15invariant_module_name\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:"invariant_module_name"\x123\n\x0finvariant_route\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"invariant_route":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1c\n\x1aMsgVerifyInvariantResponse2v\n\x03Msg\x12o\n\x0fVerifyInvariant\x12).cosmos.crisis.v1beta1.MsgVerifyInvariant\x1a1.cosmos.crisis.v1beta1.MsgVerifyInvariantResponseB-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crisis.v1beta1.tx_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/crisis/types'
    _MSGVERIFYINVARIANT.fields_by_name['invariant_module_name']._options = None
    _MSGVERIFYINVARIANT.fields_by_name['invariant_module_name']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"invariant_module_name"'
    _MSGVERIFYINVARIANT.fields_by_name['invariant_route']._options = None
    _MSGVERIFYINVARIANT.fields_by_name['invariant_route']._serialized_options = b'\xf2\xde\x1f\x16yaml:"invariant_route"'
    _MSGVERIFYINVARIANT._options = None
    _MSGVERIFYINVARIANT._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGVERIFYINVARIANT._serialized_start = 80
    _MSGVERIFYINVARIANT._serialized_end = 244
    _MSGVERIFYINVARIANTRESPONSE._serialized_start = 246
    _MSGVERIFYINVARIANTRESPONSE._serialized_end = 274
    _MSG._serialized_start = 276
    _MSG._serialized_end = 394
