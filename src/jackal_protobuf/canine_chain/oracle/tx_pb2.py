"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63\x61nine_chain/oracle/tx.proto\x12\x13\x63\x61nine_chain.oracle\".\n\rMsgCreateFeed\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15MsgCreateFeedResponse\"<\n\rMsgUpdateFeed\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"\x17\n\x15MsgUpdateFeedResponse2\xc1\x01\n\x03Msg\x12\\\n\nCreateFeed\x12\".canine_chain.oracle.MsgCreateFeed\x1a*.canine_chain.oracle.MsgCreateFeedResponse\x12\\\n\nUpdateFeed\x12\".canine_chain.oracle.MsgUpdateFeed\x1a*.canine_chain.oracle.MsgUpdateFeedResponseB3Z1github.com/jackalLabs/canine-chain/x/oracle/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.oracle.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/jackalLabs/canine-chain/x/oracle/types'
  _globals['_MSGCREATEFEED']._serialized_start=53
  _globals['_MSGCREATEFEED']._serialized_end=99
  _globals['_MSGCREATEFEEDRESPONSE']._serialized_start=101
  _globals['_MSGCREATEFEEDRESPONSE']._serialized_end=124
  _globals['_MSGUPDATEFEED']._serialized_start=126
  _globals['_MSGUPDATEFEED']._serialized_end=186
  _globals['_MSGUPDATEFEEDRESPONSE']._serialized_start=188
  _globals['_MSGUPDATEFEEDRESPONSE']._serialized_end=211
  _globals['_MSG']._serialized_start=214
  _globals['_MSG']._serialized_end=407
# @@protoc_insertion_point(module_scope)
