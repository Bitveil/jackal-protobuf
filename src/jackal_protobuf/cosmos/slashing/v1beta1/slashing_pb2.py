
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/slashing/v1beta1/slashing.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x02\n\x14ValidatorSigningInfo\x12\x0f\n\x07address\x18\x01 \x01(\t\x12-\n\x0cstart_height\x18\x02 \x01(\x03B\x17\xf2\xde\x1f\x13yaml:"start_height"\x12-\n\x0cindex_offset\x18\x03 \x01(\x03B\x17\xf2\xde\x1f\x13yaml:"index_offset"\x12Q\n\x0cjailed_until\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1f\xf2\xde\x1f\x13yaml:"jailed_until"\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x12\n\ntombstoned\x18\x05 \x01(\x08\x12?\n\x15missed_blocks_counter\x18\x06 \x01(\x03B \xf2\xde\x1f\x1cyaml:"missed_blocks_counter":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"\x88\x04\n\x06Params\x12=\n\x14signed_blocks_window\x18\x01 \x01(\x03B\x1f\xf2\xde\x1f\x1byaml:"signed_blocks_window"\x12m\n\x15min_signed_per_window\x18\x02 \x01(\x0cBN\xf2\xde\x1f\x1cyaml:"min_signed_per_window"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12d\n\x16downtime_jail_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB)\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x1dyaml:"downtime_jail_duration"\x12w\n\x1aslash_fraction_double_sign\x18\x04 \x01(\x0cBS\xf2\xde\x1f!yaml:"slash_fraction_double_sign"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12q\n\x17slash_fraction_downtime\x18\x05 \x01(\x0cBP\xf2\xde\x1f\x1eyaml:"slash_fraction_downtime"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00B3Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.slashing_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01'
    _VALIDATORSIGNINGINFO.fields_by_name['start_height']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['start_height']._serialized_options = b'\xf2\xde\x1f\x13yaml:"start_height"'
    _VALIDATORSIGNINGINFO.fields_by_name['index_offset']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['index_offset']._serialized_options = b'\xf2\xde\x1f\x13yaml:"index_offset"'
    _VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._serialized_options = b'\xf2\xde\x1f\x13yaml:"jailed_until"\x90\xdf\x1f\x01\xc8\xde\x1f\x00'
    _VALIDATORSIGNINGINFO.fields_by_name['missed_blocks_counter']._options = None
    _VALIDATORSIGNINGINFO.fields_by_name['missed_blocks_counter']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"missed_blocks_counter"'
    _VALIDATORSIGNINGINFO._options = None
    _VALIDATORSIGNINGINFO._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _PARAMS.fields_by_name['signed_blocks_window']._options = None
    _PARAMS.fields_by_name['signed_blocks_window']._serialized_options = b'\xf2\xde\x1f\x1byaml:"signed_blocks_window"'
    _PARAMS.fields_by_name['min_signed_per_window']._options = None
    _PARAMS.fields_by_name['min_signed_per_window']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"min_signed_per_window"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['downtime_jail_duration']._options = None
    _PARAMS.fields_by_name['downtime_jail_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x1dyaml:"downtime_jail_duration"'
    _PARAMS.fields_by_name['slash_fraction_double_sign']._options = None
    _PARAMS.fields_by_name['slash_fraction_double_sign']._serialized_options = b'\xf2\xde\x1f!yaml:"slash_fraction_double_sign"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['slash_fraction_downtime']._options = None
    _PARAMS.fields_by_name['slash_fraction_downtime']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"slash_fraction_downtime"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _VALIDATORSIGNINGINFO._serialized_start = 155
    _VALIDATORSIGNINGINFO._serialized_end = 466
    _PARAMS._serialized_start = 469
    _PARAMS._serialized_end = 989
