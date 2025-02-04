"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63\x61nine_chain/oracle/feed.proto\x12\x13\x63\x61nine_chain.oracle\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"l\n\x04\x46\x65\x65\x64\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x39\n\x0blast_update\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x0c\n\x04name\x18\x04 \x01(\tB3Z1github.com/jackalLabs/canine-chain/x/oracle/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.oracle.feed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/jackalLabs/canine-chain/x/oracle/types'
  _globals['_FEED'].fields_by_name['last_update']._loaded_options = None
  _globals['_FEED'].fields_by_name['last_update']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_FEED']._serialized_start=110
  _globals['_FEED']._serialized_end=218
# @@protoc_insertion_point(module_scope)
