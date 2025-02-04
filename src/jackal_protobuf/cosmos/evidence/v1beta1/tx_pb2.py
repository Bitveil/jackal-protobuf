
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/evidence/v1beta1/tx.proto\x12\x17cosmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto"f\n\x11MsgSubmitEvidence\x12\x11\n\tsubmitter\x18\x01 \x01(\t\x124\n\x08evidence\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08Evidence:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00")\n\x19MsgSubmitEvidenceResponse\x12\x0c\n\x04hash\x18\x04 \x01(\x0c2w\n\x03Msg\x12p\n\x0eSubmitEvidence\x12*.cosmos.evidence.v1beta1.MsgSubmitEvidence\x1a2.cosmos.evidence.v1beta1.MsgSubmitEvidenceResponseB3Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.tx_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01'
    _MSGSUBMITEVIDENCE.fields_by_name['evidence']._options = None
    _MSGSUBMITEVIDENCE.fields_by_name['evidence']._serialized_options = b'\xca\xb4-\x08Evidence'
    _MSGSUBMITEVIDENCE._options = None
    _MSGSUBMITEVIDENCE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGSUBMITEVIDENCE._serialized_start = 137
    _MSGSUBMITEVIDENCE._serialized_end = 239
    _MSGSUBMITEVIDENCERESPONSE._serialized_start = 241
    _MSGSUBMITEVIDENCERESPONSE._serialized_end = 282
    _MSG._serialized_start = 284
    _MSG._serialized_end = 403
