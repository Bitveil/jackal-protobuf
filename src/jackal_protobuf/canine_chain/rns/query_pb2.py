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
from jackal_protobuf.canine_chain.rns import params_pb2 as canine__chain_dot_rns_dot_params__pb2
from jackal_protobuf.canine_chain.rns import whois_pb2 as canine__chain_dot_rns_dot_whois__pb2
from jackal_protobuf.canine_chain.rns import names_pb2 as canine__chain_dot_rns_dot_names__pb2
from jackal_protobuf.canine_chain.rns import bids_pb2 as canine__chain_dot_rns_dot_bids__pb2
from jackal_protobuf.canine_chain.rns import forsale_pb2 as canine__chain_dot_rns_dot_forsale__pb2
from jackal_protobuf.canine_chain.rns import init_pb2 as canine__chain_dot_rns_dot_init__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63\x61nine_chain/rns/query.proto\x12\x10\x63\x61nine_chain.rns\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1d\x63\x61nine_chain/rns/params.proto\x1a\x1c\x63\x61nine_chain/rns/whois.proto\x1a\x1c\x63\x61nine_chain/rns/names.proto\x1a\x1b\x63\x61nine_chain/rns/bids.proto\x1a\x1e\x63\x61nine_chain/rns/forsale.proto\x1a\x1b\x63\x61nine_chain/rns/init.proto\"\r\n\x0bQueryParams\"E\n\x13QueryParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b\x32\x18.canine_chain.rns.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\tQueryName\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x11QueryNameResponse\x12+\n\x04name\x18\x01 \x01(\x0b\x32\x17.canine_chain.rns.NamesB\x04\xc8\xde\x1f\x00\"!\n\x10QueryPrimaryName\x12\r\n\x05owner\x18\x01 \x01(\t\"G\n\x18QueryPrimaryNameResponse\x12+\n\x04name\x18\x01 \x01(\x0b\x32\x17.canine_chain.rns.NamesB\x04\xc8\xde\x1f\x00\"b\n\x13QueryListOwnedNames\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x88\x01\n\x1bQueryListOwnedNamesResponse\x12,\n\x05names\x18\x01 \x03(\x0b\x32\x17.canine_chain.rns.NamesB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"K\n\rQueryAllNames\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x81\x01\n\x15QueryAllNamesResponse\x12+\n\x04name\x18\x01 \x03(\x0b\x32\x17.canine_chain.rns.NamesB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x18\n\x08QueryBid\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x10QueryBidResponse\x12*\n\x04\x62ids\x18\x01 \x01(\x0b\x32\x16.canine_chain.rns.BidsB\x04\xc8\xde\x1f\x00\"J\n\x0cQueryAllBids\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x7f\n\x14QueryAllBidsResponse\x12*\n\x04\x62ids\x18\x01 \x03(\x0b\x32\x16.canine_chain.rns.BidsB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1c\n\x0cQueryForSale\x12\x0c\n\x04name\x18\x01 \x01(\t\"I\n\x14QueryForSaleResponse\x12\x31\n\x08\x66or_sale\x18\x01 \x01(\x0b\x32\x19.canine_chain.rns.ForsaleB\x04\xc8\xde\x1f\x00\"M\n\x0fQueryAllForSale\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x89\x01\n\x17QueryAllForSaleResponse\x12\x31\n\x08\x66or_sale\x18\x01 \x03(\x0b\x32\x19.canine_chain.rns.ForsaleB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1c\n\tQueryInit\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"!\n\x11QueryInitResponse\x12\x0c\n\x04init\x18\x01 \x01(\x08\"K\n\rQueryAllInits\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x80\x01\n\x15QueryAllInitsResponse\x12*\n\x04init\x18\x01 \x03(\x0b\x32\x16.canine_chain.rns.InitB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xa4\x0b\n\x05Query\x12w\n\x06Params\x12\x1d.canine_chain.rns.QueryParams\x1a%.canine_chain.rns.QueryParamsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/jackal/canine-chain/rns/params\x12w\n\x04Name\x12\x1b.canine_chain.rns.QueryName\x1a#.canine_chain.rns.QueryNameResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/jackal/canine-chain/rns/names/{name}\x12\xa3\x01\n\x0eListOwnedNames\x12%.canine_chain.rns.QueryListOwnedNames\x1a-.canine_chain.rns.QueryListOwnedNamesResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/jackal/canine-chain/rns/list_owned_names/{address}\x12|\n\x08\x41llNames\x12\x1f.canine_chain.rns.QueryAllNames\x1a\'.canine_chain.rns.QueryAllNamesResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/jackal/canine-chain/rns/names\x12s\n\x03\x42id\x12\x1a.canine_chain.rns.QueryBid\x1a\".canine_chain.rns.QueryBidResponse\",\x82\xd3\xe4\x93\x02&\x12$/jackal/canine-chain/rns/bids/{name}\x12x\n\x07\x41llBids\x12\x1e.canine_chain.rns.QueryAllBids\x1a&.canine_chain.rns.QueryAllBidsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/jackal/canine-chain/rns/bids\x12\x83\x01\n\x07\x46orSale\x12\x1e.canine_chain.rns.QueryForSale\x1a&.canine_chain.rns.QueryForSaleResponse\"0\x82\xd3\xe4\x93\x02*\x12(/jackal/canine-chain/rns/for_sale/{name}\x12\x85\x01\n\nAllForSale\x12!.canine_chain.rns.QueryAllForSale\x1a).canine_chain.rns.QueryAllForSaleResponse\")\x82\xd3\xe4\x93\x02#\x12!/jackal/canine-chain/rns/for_sale\x12y\n\x04Init\x12\x1b.canine_chain.rns.QueryInit\x1a#.canine_chain.rns.QueryInitResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/jackal/canine-chain/rns/init/{address}\x12{\n\x08\x41llInits\x12\x1f.canine_chain.rns.QueryAllInits\x1a\'.canine_chain.rns.QueryAllInitsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/jackal/canine-chain/rns/init\x12\x8f\x01\n\x0bPrimaryName\x12\".canine_chain.rns.QueryPrimaryName\x1a*.canine_chain.rns.QueryPrimaryNameResponse\"0\x82\xd3\xe4\x93\x02*\x12(/jackal/canine-chain/rns/primary/{owner}B0Z.github.com/jackalLabs/canine-chain/x/rns/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.rns.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/jackalLabs/canine-chain/x/rns/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYNAMERESPONSE'].fields_by_name['name']._loaded_options = None
  _globals['_QUERYNAMERESPONSE'].fields_by_name['name']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPRIMARYNAMERESPONSE'].fields_by_name['name']._loaded_options = None
  _globals['_QUERYPRIMARYNAMERESPONSE'].fields_by_name['name']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYLISTOWNEDNAMESRESPONSE'].fields_by_name['names']._loaded_options = None
  _globals['_QUERYLISTOWNEDNAMESRESPONSE'].fields_by_name['names']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLNAMESRESPONSE'].fields_by_name['name']._loaded_options = None
  _globals['_QUERYALLNAMESRESPONSE'].fields_by_name['name']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYBIDRESPONSE'].fields_by_name['bids']._loaded_options = None
  _globals['_QUERYBIDRESPONSE'].fields_by_name['bids']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLBIDSRESPONSE'].fields_by_name['bids']._loaded_options = None
  _globals['_QUERYALLBIDSRESPONSE'].fields_by_name['bids']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYFORSALERESPONSE'].fields_by_name['for_sale']._loaded_options = None
  _globals['_QUERYFORSALERESPONSE'].fields_by_name['for_sale']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLFORSALERESPONSE'].fields_by_name['for_sale']._loaded_options = None
  _globals['_QUERYALLFORSALERESPONSE'].fields_by_name['for_sale']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLINITSRESPONSE'].fields_by_name['init']._loaded_options = None
  _globals['_QUERYALLINITSRESPONSE'].fields_by_name['init']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002!\022\037/jackal/canine-chain/rns/params'
  _globals['_QUERY'].methods_by_name['Name']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Name']._serialized_options = b'\202\323\344\223\002\'\022%/jackal/canine-chain/rns/names/{name}'
  _globals['_QUERY'].methods_by_name['ListOwnedNames']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ListOwnedNames']._serialized_options = b'\202\323\344\223\0025\0223/jackal/canine-chain/rns/list_owned_names/{address}'
  _globals['_QUERY'].methods_by_name['AllNames']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllNames']._serialized_options = b'\202\323\344\223\002 \022\036/jackal/canine-chain/rns/names'
  _globals['_QUERY'].methods_by_name['Bid']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Bid']._serialized_options = b'\202\323\344\223\002&\022$/jackal/canine-chain/rns/bids/{name}'
  _globals['_QUERY'].methods_by_name['AllBids']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllBids']._serialized_options = b'\202\323\344\223\002\037\022\035/jackal/canine-chain/rns/bids'
  _globals['_QUERY'].methods_by_name['ForSale']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ForSale']._serialized_options = b'\202\323\344\223\002*\022(/jackal/canine-chain/rns/for_sale/{name}'
  _globals['_QUERY'].methods_by_name['AllForSale']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllForSale']._serialized_options = b'\202\323\344\223\002#\022!/jackal/canine-chain/rns/for_sale'
  _globals['_QUERY'].methods_by_name['Init']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Init']._serialized_options = b'\202\323\344\223\002)\022\'/jackal/canine-chain/rns/init/{address}'
  _globals['_QUERY'].methods_by_name['AllInits']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllInits']._serialized_options = b'\202\323\344\223\002\037\022\035/jackal/canine-chain/rns/init'
  _globals['_QUERY'].methods_by_name['PrimaryName']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PrimaryName']._serialized_options = b'\202\323\344\223\002*\022(/jackal/canine-chain/rns/primary/{owner}'
  _globals['_QUERYPARAMS']._serialized_start=327
  _globals['_QUERYPARAMS']._serialized_end=340
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=342
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=411
  _globals['_QUERYNAME']._serialized_start=413
  _globals['_QUERYNAME']._serialized_end=438
  _globals['_QUERYNAMERESPONSE']._serialized_start=440
  _globals['_QUERYNAMERESPONSE']._serialized_end=504
  _globals['_QUERYPRIMARYNAME']._serialized_start=506
  _globals['_QUERYPRIMARYNAME']._serialized_end=539
  _globals['_QUERYPRIMARYNAMERESPONSE']._serialized_start=541
  _globals['_QUERYPRIMARYNAMERESPONSE']._serialized_end=612
  _globals['_QUERYLISTOWNEDNAMES']._serialized_start=614
  _globals['_QUERYLISTOWNEDNAMES']._serialized_end=712
  _globals['_QUERYLISTOWNEDNAMESRESPONSE']._serialized_start=715
  _globals['_QUERYLISTOWNEDNAMESRESPONSE']._serialized_end=851
  _globals['_QUERYALLNAMES']._serialized_start=853
  _globals['_QUERYALLNAMES']._serialized_end=928
  _globals['_QUERYALLNAMESRESPONSE']._serialized_start=931
  _globals['_QUERYALLNAMESRESPONSE']._serialized_end=1060
  _globals['_QUERYBID']._serialized_start=1062
  _globals['_QUERYBID']._serialized_end=1086
  _globals['_QUERYBIDRESPONSE']._serialized_start=1088
  _globals['_QUERYBIDRESPONSE']._serialized_end=1150
  _globals['_QUERYALLBIDS']._serialized_start=1152
  _globals['_QUERYALLBIDS']._serialized_end=1226
  _globals['_QUERYALLBIDSRESPONSE']._serialized_start=1228
  _globals['_QUERYALLBIDSRESPONSE']._serialized_end=1355
  _globals['_QUERYFORSALE']._serialized_start=1357
  _globals['_QUERYFORSALE']._serialized_end=1385
  _globals['_QUERYFORSALERESPONSE']._serialized_start=1387
  _globals['_QUERYFORSALERESPONSE']._serialized_end=1460
  _globals['_QUERYALLFORSALE']._serialized_start=1462
  _globals['_QUERYALLFORSALE']._serialized_end=1539
  _globals['_QUERYALLFORSALERESPONSE']._serialized_start=1542
  _globals['_QUERYALLFORSALERESPONSE']._serialized_end=1679
  _globals['_QUERYINIT']._serialized_start=1681
  _globals['_QUERYINIT']._serialized_end=1709
  _globals['_QUERYINITRESPONSE']._serialized_start=1711
  _globals['_QUERYINITRESPONSE']._serialized_end=1744
  _globals['_QUERYALLINITS']._serialized_start=1746
  _globals['_QUERYALLINITS']._serialized_end=1821
  _globals['_QUERYALLINITSRESPONSE']._serialized_start=1824
  _globals['_QUERYALLINITSRESPONSE']._serialized_end=1952
  _globals['_QUERY']._serialized_start=1955
  _globals['_QUERY']._serialized_end=3399
# @@protoc_insertion_point(module_scope)
