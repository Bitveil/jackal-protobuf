"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from jackal_protobuf.canine_chain.jklmint import params_pb2 as canine__chain_dot_jklmint_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n canine_chain/jklmint/query.proto\x12\x14\x63\x61nine_chain.jklmint\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!canine_chain/jklmint/params.proto\"\r\n\x0bQueryParams\"I\n\x13QueryParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.canine_chain.jklmint.ParamsB\x04\xc8\xde\x1f\x00\"\x10\n\x0eQueryInflation\"[\n\x16QueryInflationResponse\x12\x41\n\tinflation\x18\x01 \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\"\"\n\x11QueryMintedTokens\x12\r\n\x05\x62lock\x18\x01 \x01(\x03\"+\n\x19QueryMintedTokensResponse\x12\x0e\n\x06tokens\x18\x01 \x01(\x03\x32\xab\x03\n\x05Query\x12{\n\x06Params\x12!.canine_chain.jklmint.QueryParams\x1a).canine_chain.jklmint.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params\x12\x87\x01\n\tInflation\x12$.canine_chain.jklmint.QueryInflation\x1a,.canine_chain.jklmint.QueryInflationResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation\x12\x9a\x01\n\x0cMintedTokens\x12\'.canine_chain.jklmint.QueryMintedTokens\x1a/.canine_chain.jklmint.QueryMintedTokensResponse\"0\x82\xd3\xe4\x93\x02*\x12(/jackal/canine-chain/mint/minted/{block}B4Z2github.com/jackalLabs/canine-chain/x/jklmint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.jklmint.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/jklmint/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYINFLATIONRESPONSE'].fields_by_name['inflation']._loaded_options = None
  _globals['_QUERYINFLATIONRESPONSE'].fields_by_name['inflation']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/mint/v1beta1/params'
  _globals['_QUERY'].methods_by_name['Inflation']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Inflation']._serialized_options = b'\202\323\344\223\002 \022\036/cosmos/mint/v1beta1/inflation'
  _globals['_QUERY'].methods_by_name['MintedTokens']._loaded_options = None
  _globals['_QUERY'].methods_by_name['MintedTokens']._serialized_options = b'\202\323\344\223\002*\022(/jackal/canine-chain/mint/minted/{block}'
  _globals['_QUERYPARAMS']._serialized_start=145
  _globals['_QUERYPARAMS']._serialized_end=158
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=160
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=233
  _globals['_QUERYINFLATION']._serialized_start=235
  _globals['_QUERYINFLATION']._serialized_end=251
  _globals['_QUERYINFLATIONRESPONSE']._serialized_start=253
  _globals['_QUERYINFLATIONRESPONSE']._serialized_end=344
  _globals['_QUERYMINTEDTOKENS']._serialized_start=346
  _globals['_QUERYMINTEDTOKENS']._serialized_end=380
  _globals['_QUERYMINTEDTOKENSRESPONSE']._serialized_start=382
  _globals['_QUERYMINTEDTOKENSRESPONSE']._serialized_end=425
  _globals['_QUERY']._serialized_start=428
  _globals['_QUERY']._serialized_end=855
# @@protoc_insertion_point(module_scope)
