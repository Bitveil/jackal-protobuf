"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!canine_chain/jklmint/params.proto\x12\x14\x63\x61nine_chain.jklmint\x1a\x14gogoproto/gogo.proto\"\x8f\x03\n\x06Params\x12)\n\nmint_denom\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"mint_denom\"\x12\x35\n\x10\x64\x65v_grants_ratio\x18\x02 \x01(\x03\x42\x1b\xf2\xde\x1f\x17yaml:\"dev_grants_ratio\"\x12-\n\x0cstaker_ratio\x18\x03 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"staker_ratio\"\x12\x35\n\x10tokens_per_block\x18\x04 \x01(\x03\x42\x1b\xf2\xde\x1f\x17yaml:\"tokens_per_block\"\x12/\n\rmint_decrease\x18\x05 \x01(\x03\x42\x18\xf2\xde\x1f\x14yaml:\"mint_decrease\"\x12\x43\n\x17storage_stipend_address\x18\x06 \x01(\tB\"\xf2\xde\x1f\x1eyaml:\"storage_stipend_address\"\x12\x41\n\x16storage_provider_ratio\x18\x07 \x01(\x03\x42!\xf2\xde\x1f\x1dyaml:\"storage_provider_ratio\":\x04\x98\xa0\x1f\x00\x42\x34Z2github.com/jackalLabs/canine-chain/x/jklmint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.jklmint.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/jklmint/types'
  _globals['_PARAMS'].fields_by_name['mint_denom']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['mint_denom']._serialized_options = b'\362\336\037\021yaml:\"mint_denom\"'
  _globals['_PARAMS'].fields_by_name['dev_grants_ratio']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['dev_grants_ratio']._serialized_options = b'\362\336\037\027yaml:\"dev_grants_ratio\"'
  _globals['_PARAMS'].fields_by_name['staker_ratio']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['staker_ratio']._serialized_options = b'\362\336\037\023yaml:\"staker_ratio\"'
  _globals['_PARAMS'].fields_by_name['tokens_per_block']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['tokens_per_block']._serialized_options = b'\362\336\037\027yaml:\"tokens_per_block\"'
  _globals['_PARAMS'].fields_by_name['mint_decrease']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['mint_decrease']._serialized_options = b'\362\336\037\024yaml:\"mint_decrease\"'
  _globals['_PARAMS'].fields_by_name['storage_stipend_address']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['storage_stipend_address']._serialized_options = b'\362\336\037\036yaml:\"storage_stipend_address\"'
  _globals['_PARAMS'].fields_by_name['storage_provider_ratio']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['storage_provider_ratio']._serialized_options = b'\362\336\037\035yaml:\"storage_provider_ratio\"'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\230\240\037\000'
  _globals['_PARAMS']._serialized_start=82
  _globals['_PARAMS']._serialized_end=481
# @@protoc_insertion_point(module_scope)
