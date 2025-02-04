
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/genutil/v1beta1/genesis.proto\x12\x16cosmos.genutil.v1beta1\x1a\x14gogoproto/gogo.proto"X\n\x0cGenesisState\x12H\n\x07gen_txs\x18\x01 \x03(\x0cB7\xfa\xde\x1f\x18encoding/json.RawMessage\xea\xde\x1f\x06gentxs\xf2\xde\x1f\ryaml:"gentxs"B.Z,github.com/cosmos/cosmos-sdk/x/genutil/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.genutil.v1beta1.genesis_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/genutil/types'
    _GENESISSTATE.fields_by_name['gen_txs']._options = None
    _GENESISSTATE.fields_by_name['gen_txs']._serialized_options = b'\xfa\xde\x1f\x18encoding/json.RawMessage\xea\xde\x1f\x06gentxs\xf2\xde\x1f\ryaml:"gentxs"'
    _GENESISSTATE._serialized_start = 86
    _GENESISSTATE._serialized_end = 174
