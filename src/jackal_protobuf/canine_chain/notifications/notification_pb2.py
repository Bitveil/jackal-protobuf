"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-canine_chain/notifications/notification.proto\x12\x1a\x63\x61nine_chain.notifications\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"b\n\x0cNotification\x12\n\n\x02to\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x10\n\x08\x63ontents\x18\x04 \x01(\t\x12\x18\n\x10private_contents\x18\x05 \x01(\x0c\"1\n\x05\x42lock\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x17\n\x0f\x62locked_address\x18\x02 \x01(\tB:Z8github.com/jackalLabs/canine-chain/x/notifications/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.notifications.notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/jackalLabs/canine-chain/x/notifications/types'
  _globals['_NOTIFICATION']._serialized_start=132
  _globals['_NOTIFICATION']._serialized_end=230
  _globals['_BLOCK']._serialized_start=232
  _globals['_BLOCK']._serialized_end=281
# @@protoc_insertion_point(module_scope)
