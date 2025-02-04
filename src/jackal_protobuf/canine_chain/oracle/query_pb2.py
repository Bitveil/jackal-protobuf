"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...canine_chain.oracle import params_pb2 as canine__chain_dot_oracle_dot_params__pb2
from ...canine_chain.oracle import feed_pb2 as canine__chain_dot_oracle_dot_feed__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63\x61nine_chain/oracle/query.proto\x12\x13\x63\x61nine_chain.oracle\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a canine_chain/oracle/params.proto\x1a\x1e\x63\x61nine_chain/oracle/feed.proto\"\r\n\x0bQueryParams\"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.canine_chain.oracle.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\tQueryFeed\x12\x0c\n\x04name\x18\x01 \x01(\t\"B\n\x11QueryFeedResponse\x12-\n\x04\x66\x65\x65\x64\x18\x01 \x01(\x0b\x32\x19.canine_chain.oracle.FeedB\x04\xc8\xde\x1f\x00\"K\n\rQueryAllFeeds\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x83\x01\n\x15QueryAllFeedsResponse\x12-\n\x04\x66\x65\x65\x64\x18\x01 \x03(\x0b\x32\x19.canine_chain.oracle.FeedB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x95\x03\n\x05Query\x12\x80\x01\n\x06Params\x12 .canine_chain.oracle.QueryParams\x1a(.canine_chain.oracle.QueryParamsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/jackal/canine-chain/oracle/params\x12\x80\x01\n\x04\x46\x65\x65\x64\x12\x1e.canine_chain.oracle.QueryFeed\x1a&.canine_chain.oracle.QueryFeedResponse\"0\x82\xd3\xe4\x93\x02*\x12(/jackal/canine-chain/oracle/feeds/{name}\x12\x85\x01\n\x08\x41llFeeds\x12\".canine_chain.oracle.QueryAllFeeds\x1a*.canine_chain.oracle.QueryAllFeedsResponse\")\x82\xd3\xe4\x93\x02#\x12!/jackal/canine-chain/oracle/feedsB3Z1github.com/jackalLabs/canine-chain/x/oracle/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.oracle.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/jackalLabs/canine-chain/x/oracle/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYFEEDRESPONSE'].fields_by_name['feed']._loaded_options = None
  _globals['_QUERYFEEDRESPONSE'].fields_by_name['feed']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLFEEDSRESPONSE'].fields_by_name['feed']._loaded_options = None
  _globals['_QUERYALLFEEDSRESPONSE'].fields_by_name['feed']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002$\022\"/jackal/canine-chain/oracle/params'
  _globals['_QUERY'].methods_by_name['Feed']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Feed']._serialized_options = b'\202\323\344\223\002*\022(/jackal/canine-chain/oracle/feeds/{name}'
  _globals['_QUERY'].methods_by_name['AllFeeds']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllFeeds']._serialized_options = b'\202\323\344\223\002#\022!/jackal/canine-chain/oracle/feeds'
  _globals['_QUERYPARAMS']._serialized_start=218
  _globals['_QUERYPARAMS']._serialized_end=231
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=233
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=305
  _globals['_QUERYFEED']._serialized_start=307
  _globals['_QUERYFEED']._serialized_end=332
  _globals['_QUERYFEEDRESPONSE']._serialized_start=334
  _globals['_QUERYFEEDRESPONSE']._serialized_end=400
  _globals['_QUERYALLFEEDS']._serialized_start=402
  _globals['_QUERYALLFEEDS']._serialized_end=477
  _globals['_QUERYALLFEEDSRESPONSE']._serialized_start=480
  _globals['_QUERYALLFEEDSRESPONSE']._serialized_end=611
  _globals['_QUERY']._serialized_start=614
  _globals['_QUERY']._serialized_end=1019
# @@protoc_insertion_point(module_scope)
