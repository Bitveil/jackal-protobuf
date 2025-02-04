"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from jackal_protobuf.canine_chain.jklmint import params_pb2 as canine__chain_dot_jklmint_dot_params__pb2
from jackal_protobuf.jklmint import minted_block_pb2 as canine__chain_dot_jklmint_dot_minted__block__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"canine_chain/jklmint/genesis.proto\x12\x14\x63\x61nine_chain.jklmint\x1a\x14gogoproto/gogo.proto\x1a!canine_chain/jklmint/params.proto\x1a\'canine_chain/jklmint/minted_block.proto\"\x82\x01\n\x0cGenesisState\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.canine_chain.jklmint.ParamsB\x04\xc8\xde\x1f\x00\x12>\n\rminted_blocks\x18\x02 \x01(\x0b\x32!.canine_chain.jklmint.MintedBlockB\x04\xc8\xde\x1f\x00\x42\x34Z2github.com/jackalLabs/canine-chain/x/jklmint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.jklmint.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/jklmint/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['minted_blocks']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['minted_blocks']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=159
  _globals['_GENESISSTATE']._serialized_end=289
# @@protoc_insertion_point(module_scope)
