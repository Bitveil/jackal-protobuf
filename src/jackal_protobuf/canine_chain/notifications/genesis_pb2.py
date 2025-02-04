"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from jackal_protobuf.canine_chain.notifications import params_pb2 as canine__chain_dot_notifications_dot_params__pb2
from jackal_protobuf.canine_chain.notifications import notification_pb2 as canine__chain_dot_notifications_dot_notification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(canine_chain/notifications/genesis.proto\x12\x1a\x63\x61nine_chain.notifications\x1a\x14gogoproto/gogo.proto\x1a\'canine_chain/notifications/params.proto\x1a-canine_chain/notifications/notification.proto\"\x8f\x01\n\x0cGenesisState\x12\x38\n\x06params\x18\x01 \x01(\x0b\x32\".canine_chain.notifications.ParamsB\x04\xc8\xde\x1f\x00\x12\x45\n\rnotifications\x18\x02 \x03(\x0b\x32(.canine_chain.notifications.NotificationB\x04\xc8\xde\x1f\x00\x42:Z8github.com/jackalLabs/canine-chain/x/notifications/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.notifications.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/jackalLabs/canine-chain/x/notifications/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['notifications']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['notifications']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=183
  _globals['_GENESISSTATE']._serialized_end=326
# @@protoc_insertion_point(module_scope)
