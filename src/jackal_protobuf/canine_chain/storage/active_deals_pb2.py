"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'canine_chain/storage/active_deals.proto\x12\x14\x63\x61nine_chain.storage\"\xe8\x01\n\x11LegacyActiveDeals\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0e\n\x06signee\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x12\n\nstartblock\x18\x04 \x01(\t\x12\x10\n\x08\x65ndblock\x18\x05 \x01(\t\x12\x10\n\x08\x66ilesize\x18\x06 \x01(\t\x12\x12\n\nlast_proof\x18\x07 \x01(\x03\x12\x14\n\x0cproofsmissed\x18\x08 \x01(\t\x12\x14\n\x0c\x62locktoprove\x18\t \x01(\t\x12\x0f\n\x07\x63reator\x18\n \x01(\t\x12\x0e\n\x06merkle\x18\x0b \x01(\t\x12\x0b\n\x03\x66id\x18\x0c \x01(\t\"\xbd\x01\n\x0bUnifiedFile\x12\x0e\n\x06merkle\x18\x01 \x01(\x0c\x12\r\n\x05owner\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0f\n\x07\x65xpires\x18\x04 \x01(\x03\x12\x11\n\tfile_size\x18\x05 \x01(\x03\x12\x16\n\x0eproof_interval\x18\x06 \x01(\x03\x12\x12\n\nproof_type\x18\x07 \x01(\x03\x12\x0e\n\x06proofs\x18\x08 \x03(\t\x12\x12\n\nmax_proofs\x18\t \x01(\x03\x12\x0c\n\x04note\x18\n \x01(\t\"v\n\tFileProof\x12\x0e\n\x06prover\x18\x01 \x01(\t\x12\x0e\n\x06merkle\x18\x02 \x01(\x0c\x12\r\n\x05owner\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x13\n\x0blast_proven\x18\x05 \x01(\x03\x12\x16\n\x0e\x63hunk_to_prove\x18\x06 \x01(\x03\x42\x34Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.active_deals_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_LEGACYACTIVEDEALS']._serialized_start=66
  _globals['_LEGACYACTIVEDEALS']._serialized_end=298
  _globals['_UNIFIEDFILE']._serialized_start=301
  _globals['_UNIFIEDFILE']._serialized_end=490
  _globals['_FILEPROOF']._serialized_start=492
  _globals['_FILEPROOF']._serialized_end=610
# @@protoc_insertion_point(module_scope)
