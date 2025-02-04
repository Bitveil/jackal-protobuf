"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from jackal_protobuf.canine_chain.oracle import params_pb2 as canine__chain_dot_oracle_dot_params__pb2
from jackal_protobuf.canine_chain.oracle import feed_pb2 as canine__chain_dot_oracle_dot_feed__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!canine_chain/oracle/genesis.proto\x12\x13\x63\x61nine_chain.oracle\x1a\x14gogoproto/gogo.proto\x1a canine_chain/oracle/params.proto\x1a\x1e\x63\x61nine_chain/oracle/feed.proto\"u\n\x0cGenesisState\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.canine_chain.oracle.ParamsB\x04\xc8\xde\x1f\x00\x12\x32\n\tfeed_list\x18\x02 \x03(\x0b\x32\x19.canine_chain.oracle.FeedB\x04\xc8\xde\x1f\x00\x42\x33Z1github.com/jackalLabs/canine-chain/x/oracle/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.oracle.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/jackalLabs/canine-chain/x/oracle/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['feed_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['feed_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=146
  _globals['_GENESISSTATE']._serialized_end=263
# @@protoc_insertion_point(module_scope)
