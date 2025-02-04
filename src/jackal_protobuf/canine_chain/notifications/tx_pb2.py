"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from jackal_protobuf.canine_chain.notifications import notification_pb2 as canine__chain_dot_notifications_dot_notification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#canine_chain/notifications/tx.proto\x12\x1a\x63\x61nine_chain.notifications\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-canine_chain/notifications/notification.proto\"`\n\x15MsgCreateNotification\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x10\n\x08\x63ontents\x18\x03 \x01(\t\x12\x18\n\x10private_contents\x18\x04 \x01(\x0c\"\x1f\n\x1dMsgCreateNotificationResponse\"D\n\x15MsgDeleteNotification\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\"\x1f\n\x1dMsgDeleteNotificationResponse\"4\n\x0fMsgBlockSenders\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x10\n\x08to_block\x18\x02 \x03(\t\"\x19\n\x17MsgBlockSendersResponse2\x81\x03\n\x03Msg\x12\x82\x01\n\x12\x43reateNotification\x12\x31.canine_chain.notifications.MsgCreateNotification\x1a\x39.canine_chain.notifications.MsgCreateNotificationResponse\x12\x82\x01\n\x12\x44\x65leteNotification\x12\x31.canine_chain.notifications.MsgDeleteNotification\x1a\x39.canine_chain.notifications.MsgDeleteNotificationResponse\x12p\n\x0c\x42lockSenders\x12+.canine_chain.notifications.MsgBlockSenders\x1a\x33.canine_chain.notifications.MsgBlockSendersResponseB:Z8github.com/jackalLabs/canine-chain/x/notifications/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.notifications.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/jackalLabs/canine-chain/x/notifications/types'
  _globals['_MSGCREATENOTIFICATION']._serialized_start=169
  _globals['_MSGCREATENOTIFICATION']._serialized_end=265
  _globals['_MSGCREATENOTIFICATIONRESPONSE']._serialized_start=267
  _globals['_MSGCREATENOTIFICATIONRESPONSE']._serialized_end=298
  _globals['_MSGDELETENOTIFICATION']._serialized_start=300
  _globals['_MSGDELETENOTIFICATION']._serialized_end=368
  _globals['_MSGDELETENOTIFICATIONRESPONSE']._serialized_start=370
  _globals['_MSGDELETENOTIFICATIONRESPONSE']._serialized_end=401
  _globals['_MSGBLOCKSENDERS']._serialized_start=403
  _globals['_MSGBLOCKSENDERS']._serialized_end=455
  _globals['_MSGBLOCKSENDERSRESPONSE']._serialized_start=457
  _globals['_MSGBLOCKSENDERSRESPONSE']._serialized_end=482
  _globals['_MSG']._serialized_start=485
  _globals['_MSG']._serialized_end=870
# @@protoc_insertion_point(module_scope)
