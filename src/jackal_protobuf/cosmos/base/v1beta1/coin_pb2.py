
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()

try:
    from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
except TypeError:
    pass

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/base/v1beta1/coin.proto\x12\x13cosmos.base.v1beta1\x1a\x14gogoproto/gogo.proto"8\n\x04Coin\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x1b\n\x06amount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01";\n\x07DecCoin\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x1b\n\x06amount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01"$\n\x08IntProto\x12\x18\n\x03int\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00"$\n\x08DecProto\x12\x18\n\x03dec\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00B,Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.v1beta1.coin_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00'
    _COIN.fields_by_name['amount']._options = None
    _COIN.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f\x03Int\xc8\xde\x1f\x00'
    _COIN._options = None
    _COIN._serialized_options = b'\xe8\xa0\x1f\x01'
    _DECCOIN.fields_by_name['amount']._options = None
    _DECCOIN.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00'
    _DECCOIN._options = None
    _DECCOIN._serialized_options = b'\xe8\xa0\x1f\x01'
    _INTPROTO.fields_by_name['int']._options = None
    _INTPROTO.fields_by_name['int']._serialized_options = b'\xda\xde\x1f\x03Int\xc8\xde\x1f\x00'
    _DECPROTO.fields_by_name['dec']._options = None
    _DECPROTO.fields_by_name['dec']._serialized_options = b'\xda\xde\x1f\x03Dec\xc8\xde\x1f\x00'
    _COIN._serialized_start = 77
    _COIN._serialized_end = 133
    _DECCOIN._serialized_start = 135
    _DECCOIN._serialized_end = 194
    _INTPROTO._serialized_start = 196
    _INTPROTO._serialized_end = 232
    _DECPROTO._serialized_start = 234
    _DECPROTO._serialized_end = 270
