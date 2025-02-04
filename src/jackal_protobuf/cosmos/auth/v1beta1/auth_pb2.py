
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/auth/v1beta1/auth.proto\x12\x13cosmos.auth.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xd3\x01\n\x0bBaseAccount\x12\x0f\n\x07address\x18\x01 \x01(\t\x12T\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB-\xea\xde\x1f\x14public_key,omitempty\xf2\xde\x1f\x11yaml:"public_key"\x121\n\x0eaccount_number\x18\x03 \x01(\x04B\x19\xf2\xde\x1f\x15yaml:"account_number"\x12\x10\n\x08sequence\x18\x04 \x01(\x04:\x18\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x08AccountI"\xa3\x01\n\rModuleAccount\x12S\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x1b\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:"base_account"\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x0eModuleAccountI"\xff\x02\n\x06Params\x12;\n\x13max_memo_characters\x18\x01 \x01(\x04B\x1e\xf2\xde\x1f\x1ayaml:"max_memo_characters"\x12-\n\x0ctx_sig_limit\x18\x02 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"tx_sig_limit"\x12?\n\x15tx_size_cost_per_byte\x18\x03 \x01(\x04B \xf2\xde\x1f\x1cyaml:"tx_size_cost_per_byte"\x12[\n\x17sig_verify_cost_ed25519\x18\x04 \x01(\x04B:\xe2\xde\x1f\x14SigVerifyCostED25519\xf2\xde\x1f\x1eyaml:"sig_verify_cost_ed25519"\x12a\n\x19sig_verify_cost_secp256k1\x18\x05 \x01(\x04B>\xe2\xde\x1f\x16SigVerifyCostSecp256k1\xf2\xde\x1f yaml:"sig_verify_cost_secp256k1":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.auth.v1beta1.auth_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
    _BASEACCOUNT.fields_by_name['pub_key']._options = None
    _BASEACCOUNT.fields_by_name['pub_key']._serialized_options = b'\xea\xde\x1f\x14public_key,omitempty\xf2\xde\x1f\x11yaml:"public_key"'
    _BASEACCOUNT.fields_by_name['account_number']._options = None
    _BASEACCOUNT.fields_by_name['account_number']._serialized_options = b'\xf2\xde\x1f\x15yaml:"account_number"'
    _BASEACCOUNT._options = None
    _BASEACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x08AccountI'
    _MODULEACCOUNT.fields_by_name['base_account']._options = None
    _MODULEACCOUNT.fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:"base_account"'
    _MODULEACCOUNT._options = None
    _MODULEACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x0eModuleAccountI'
    _PARAMS.fields_by_name['max_memo_characters']._options = None
    _PARAMS.fields_by_name['max_memo_characters']._serialized_options = b'\xf2\xde\x1f\x1ayaml:"max_memo_characters"'
    _PARAMS.fields_by_name['tx_sig_limit']._options = None
    _PARAMS.fields_by_name['tx_sig_limit']._serialized_options = b'\xf2\xde\x1f\x13yaml:"tx_sig_limit"'
    _PARAMS.fields_by_name['tx_size_cost_per_byte']._options = None
    _PARAMS.fields_by_name['tx_size_cost_per_byte']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"tx_size_cost_per_byte"'
    _PARAMS.fields_by_name['sig_verify_cost_ed25519']._options = None
    _PARAMS.fields_by_name['sig_verify_cost_ed25519']._serialized_options = b'\xe2\xde\x1f\x14SigVerifyCostED25519\xf2\xde\x1f\x1eyaml:"sig_verify_cost_ed25519"'
    _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._options = None
    _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._serialized_options = b'\xe2\xde\x1f\x16SigVerifyCostSecp256k1\xf2\xde\x1f yaml:"sig_verify_cost_secp256k1"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _BASEACCOUNT._serialized_start = 132
    _BASEACCOUNT._serialized_end = 343
    _MODULEACCOUNT._serialized_start = 346
    _MODULEACCOUNT._serialized_end = 509
    _PARAMS._serialized_start = 512
    _PARAMS._serialized_end = 895
