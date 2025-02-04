"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'canine_chain/storage/payment_info.proto\x12\x14\x63\x61nine_chain.storage\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x9e\x02\n\x12StoragePaymentInfo\x12\x33\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x31\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x16\n\x0espaceAvailable\x18\x03 \x01(\x03\x12\x11\n\tspaceUsed\x18\x04 \x01(\x03\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12Z\n\x05\x63oins\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xde\x01\n\x0cPaymentGauge\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x33\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x31\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12Z\n\x05\x63oins\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsB4Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.payment_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['start']._loaded_options = None
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['start']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['end']._loaded_options = None
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['end']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['coins']._loaded_options = None
  _globals['_STORAGEPAYMENTINFO'].fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_STORAGEPAYMENTINFO']._loaded_options = None
  _globals['_STORAGEPAYMENTINFO']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_PAYMENTGAUGE'].fields_by_name['start']._loaded_options = None
  _globals['_PAYMENTGAUGE'].fields_by_name['start']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_PAYMENTGAUGE'].fields_by_name['end']._loaded_options = None
  _globals['_PAYMENTGAUGE'].fields_by_name['end']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_PAYMENTGAUGE'].fields_by_name['coins']._loaded_options = None
  _globals['_PAYMENTGAUGE'].fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_STORAGEPAYMENTINFO']._serialized_start=180
  _globals['_STORAGEPAYMENTINFO']._serialized_end=466
  _globals['_PAYMENTGAUGE']._serialized_start=469
  _globals['_PAYMENTGAUGE']._serialized_end=691
# @@protoc_insertion_point(module_scope)
