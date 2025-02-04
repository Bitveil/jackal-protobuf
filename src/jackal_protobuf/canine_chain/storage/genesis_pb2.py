"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from jackal_protobuf.canine_chain.storage import params_pb2 as canine__chain_dot_storage_dot_params__pb2
from jackal_protobuf.canine_chain.storage import active_deals_pb2 as canine__chain_dot_storage_dot_active__deals__pb2
from jackal_protobuf.canine_chain.storage import providers_pb2 as canine__chain_dot_storage_dot_providers__pb2
from jackal_protobuf.canine_chain.storage import payment_info_pb2 as canine__chain_dot_storage_dot_payment__info__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"canine_chain/storage/genesis.proto\x12\x14\x63\x61nine_chain.storage\x1a\x14gogoproto/gogo.proto\x1a!canine_chain/storage/params.proto\x1a\'canine_chain/storage/active_deals.proto\x1a$canine_chain/storage/providers.proto\x1a\'canine_chain/storage/payment_info.proto\"\xd8\x04\n\x0cGenesisState\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.canine_chain.storage.ParamsB\x04\xc8\xde\x1f\x00\x12:\n\tfile_list\x18\x02 \x03(\x0b\x32!.canine_chain.storage.UnifiedFileB\x04\xc8\xde\x1f\x00\x12=\n\x0eproviders_list\x18\x03 \x03(\x0b\x32\x1f.canine_chain.storage.ProvidersB\x04\xc8\xde\x1f\x00\x12I\n\x11payment_info_list\x18\x04 \x03(\x0b\x32(.canine_chain.storage.StoragePaymentInfoB\x04\xc8\xde\x1f\x00\x12?\n\x0f\x63ollateral_list\x18\x05 \x03(\x0b\x32 .canine_chain.storage.CollateralB\x04\xc8\xde\x1f\x00\x12J\n\x15\x61\x63tive_providers_list\x18\x06 \x03(\x0b\x32%.canine_chain.storage.ActiveProvidersB\x04\xc8\xde\x1f\x00\x12<\n\x0creport_forms\x18\x07 \x03(\x0b\x32 .canine_chain.storage.ReportFormB\x04\xc8\xde\x1f\x00\x12\x41\n\x0c\x61ttest_forms\x18\x08 \x03(\x0b\x32%.canine_chain.storage.AttestationFormB\x04\xc8\xde\x1f\x00\x12@\n\x0epayment_gauges\x18\t \x03(\x0b\x32\".canine_chain.storage.PaymentGaugeB\x04\xc8\xde\x1f\x00\x42\x34Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['file_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['file_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['providers_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['providers_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['payment_info_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['payment_info_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['collateral_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['collateral_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['active_providers_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['active_providers_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['report_forms']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['report_forms']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['attest_forms']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['attest_forms']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['payment_gauges']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['payment_gauges']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=238
  _globals['_GENESISSTATE']._serialized_end=838
# @@protoc_insertion_point(module_scope)
