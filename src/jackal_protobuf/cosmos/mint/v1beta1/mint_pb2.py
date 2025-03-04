
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/mint/v1beta1/mint.proto\x12\x13cosmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto"\xb2\x01\n\x06Minter\x12A\n\tinflation\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12e\n\x11annual_provisions\x18\x02 \x01(\tBJ\xf2\xde\x1f\x18yaml:"annual_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\xdf\x03\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12m\n\x15inflation_rate_change\x18\x02 \x01(\tBN\xf2\xde\x1f\x1cyaml:"inflation_rate_change"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12]\n\rinflation_max\x18\x03 \x01(\tBF\xf2\xde\x1f\x14yaml:"inflation_max"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12]\n\rinflation_min\x18\x04 \x01(\tBF\xf2\xde\x1f\x14yaml:"inflation_min"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Y\n\x0bgoal_bonded\x18\x05 \x01(\tBD\xf2\xde\x1f\x12yaml:"goal_bonded"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x123\n\x0fblocks_per_year\x18\x06 \x01(\x04B\x1a\xf2\xde\x1f\x16yaml:"blocks_per_year":\x04\x98\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.mint_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
    _MINTER.fields_by_name['inflation']._options = None
    _MINTER.fields_by_name['inflation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _MINTER.fields_by_name['annual_provisions']._options = None
    _MINTER.fields_by_name['annual_provisions']._serialized_options = b'\xf2\xde\x1f\x18yaml:"annual_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['inflation_rate_change']._options = None
    _PARAMS.fields_by_name['inflation_rate_change']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"inflation_rate_change"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['inflation_max']._options = None
    _PARAMS.fields_by_name['inflation_max']._serialized_options = b'\xf2\xde\x1f\x14yaml:"inflation_max"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['inflation_min']._options = None
    _PARAMS.fields_by_name['inflation_min']._serialized_options = b'\xf2\xde\x1f\x14yaml:"inflation_min"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['goal_bonded']._options = None
    _PARAMS.fields_by_name['goal_bonded']._serialized_options = b'\xf2\xde\x1f\x12yaml:"goal_bonded"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['blocks_per_year']._options = None
    _PARAMS.fields_by_name['blocks_per_year']._serialized_options = b'\xf2\xde\x1f\x16yaml:"blocks_per_year"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _MINTER._serialized_start = 78
    _MINTER._serialized_end = 256
    _PARAMS._serialized_start = 259
    _PARAMS._serialized_end = 738
