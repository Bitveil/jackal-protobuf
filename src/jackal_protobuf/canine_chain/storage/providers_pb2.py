"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$canine_chain/storage/providers.proto\x12\x14\x63\x61nine_chain.storage\"\x98\x01\n\tProviders\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x12\n\ntotalspace\x18\x03 \x01(\t\x12\x18\n\x10\x62urned_contracts\x18\x04 \x01(\t\x12\x0f\n\x07\x63reator\x18\x05 \x01(\t\x12\x18\n\x10keybase_identity\x18\x06 \x01(\t\x12\x15\n\rauth_claimers\x18\x07 \x03(\t\"\"\n\x0f\x41\x63tiveProviders\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"1\n\x0b\x41ttestation\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x10\n\x08\x63omplete\x18\x02 \x01(\x08\"\x88\x01\n\x0f\x41ttestationForm\x12\x37\n\x0c\x61ttestations\x18\x01 \x03(\x0b\x32!.canine_chain.storage.Attestation\x12\x0e\n\x06prover\x18\x02 \x01(\t\x12\x0e\n\x06merkle\x18\x03 \x01(\x0c\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\"\x83\x01\n\nReportForm\x12\x37\n\x0c\x61ttestations\x18\x01 \x03(\x0b\x32!.canine_chain.storage.Attestation\x12\x0e\n\x06prover\x18\x02 \x01(\t\x12\x0e\n\x06merkle\x18\x03 \x01(\x0c\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\"-\n\nCollateral\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x42\x34Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.providers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_PROVIDERS']._serialized_start=63
  _globals['_PROVIDERS']._serialized_end=215
  _globals['_ACTIVEPROVIDERS']._serialized_start=217
  _globals['_ACTIVEPROVIDERS']._serialized_end=251
  _globals['_ATTESTATION']._serialized_start=253
  _globals['_ATTESTATION']._serialized_end=302
  _globals['_ATTESTATIONFORM']._serialized_start=305
  _globals['_ATTESTATIONFORM']._serialized_end=441
  _globals['_REPORTFORM']._serialized_start=444
  _globals['_REPORTFORM']._serialized_end=575
  _globals['_COLLATERAL']._serialized_start=577
  _globals['_COLLATERAL']._serialized_end=622
# @@protoc_insertion_point(module_scope)
