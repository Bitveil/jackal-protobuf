"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!canine_chain/storage/params.proto\x12\x14\x63\x61nine_chain.storage\x1a\x14gogoproto/gogo.proto\"\x87\x03\n\x06Params\x12\x17\n\x0f\x64\x65posit_account\x18\x01 \x01(\t\x12\x14\n\x0cproof_window\x18\x02 \x01(\x03\x12\x12\n\nchunk_size\x18\x03 \x01(\x03\x12\x16\n\x0emisses_to_burn\x18\x04 \x01(\x03\x12\x12\n\nprice_feed\x18\x05 \x01(\t\x12\"\n\x1amax_contract_age_in_blocks\x18\x06 \x01(\x03\x12\x1e\n\x16price_per_tb_per_month\x18\x07 \x01(\x03\x12\x16\n\x0e\x61ttestFormSize\x18\x08 \x01(\x03\x12\x17\n\x0f\x61ttestMinToPass\x18\t \x01(\x03\x12\x17\n\x0f\x63ollateralPrice\x18\n \x01(\x03\x12\x14\n\x0c\x63heck_window\x18\x0b \x01(\x03\x12\'\n\tpol_ratio\x18\x0c \x01(\x03\x42\x14\xf2\xde\x1f\x10yaml:\"pol_ratio\"\x12;\n\x13referral_commission\x18\r \x01(\x03\x42\x1e\xf2\xde\x1f\x1ayaml:\"referral_commission\":\x04\x98\xa0\x1f\x00\x42\x34Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_PARAMS'].fields_by_name['pol_ratio']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['pol_ratio']._serialized_options = b'\362\336\037\020yaml:\"pol_ratio\"'
  _globals['_PARAMS'].fields_by_name['referral_commission']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['referral_commission']._serialized_options = b'\362\336\037\032yaml:\"referral_commission\"'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\230\240\037\000'
  _globals['_PARAMS']._serialized_start=82
  _globals['_PARAMS']._serialized_end=473
# @@protoc_insertion_point(module_scope)
