"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from jackal_protobuf.canine_chain.filetree import params_pb2 as canine__chain_dot_filetree_dot_params__pb2
from jackal_protobuf.canine_chain.filetree import files_pb2 as canine__chain_dot_filetree_dot_files__pb2
from jackal_protobuf.canine_chain.filetree import pubkey_pb2 as canine__chain_dot_filetree_dot_pubkey__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#canine_chain/filetree/genesis.proto\x12\x15\x63\x61nine_chain.filetree\x1a\x14gogoproto/gogo.proto\x1a\"canine_chain/filetree/params.proto\x1a!canine_chain/filetree/files.proto\x1a\"canine_chain/filetree/pubkey.proto\"\xb6\x01\n\x0cGenesisState\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1d.canine_chain.filetree.ParamsB\x04\xc8\xde\x1f\x00\x12\x36\n\nfiles_list\x18\x02 \x03(\x0b\x32\x1c.canine_chain.filetree.FilesB\x04\xc8\xde\x1f\x00\x12\x39\n\x0cpub_key_list\x18\x03 \x03(\x0b\x32\x1d.canine_chain.filetree.PubkeyB\x04\xc8\xde\x1f\x00\x42\x35Z3github.com/jackalLabs/canine-chain/x/filetree/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.filetree.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/jackalLabs/canine-chain/x/filetree/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['files_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['files_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['pub_key_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['pub_key_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=192
  _globals['_GENESISSTATE']._serialized_end=374
# @@protoc_insertion_point(module_scope)
