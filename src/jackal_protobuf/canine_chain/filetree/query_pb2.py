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
from ...canine_chain.filetree import params_pb2 as canine__chain_dot_filetree_dot_params__pb2
from ...canine_chain.filetree import files_pb2 as canine__chain_dot_filetree_dot_files__pb2
from ...canine_chain.filetree import pubkey_pb2 as canine__chain_dot_filetree_dot_pubkey__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!canine_chain/filetree/query.proto\x12\x15\x63\x61nine_chain.filetree\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\"canine_chain/filetree/params.proto\x1a!canine_chain/filetree/files.proto\x1a\"canine_chain/filetree/pubkey.proto\"\r\n\x0bQueryParams\"J\n\x13QueryParamsResponse\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1d.canine_chain.filetree.ParamsB\x04\xc8\xde\x1f\x00\"3\n\tQueryFile\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x15\n\rowner_address\x18\x02 \x01(\t\"E\n\x11QueryFileResponse\x12\x30\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x1c.canine_chain.filetree.FilesB\x04\xc8\xde\x1f\x00\"K\n\rQueryAllFiles\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x87\x01\n\x15QueryAllFilesResponse\x12\x31\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1c.canine_chain.filetree.FilesB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1e\n\x0bQueryPubKey\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"K\n\x13QueryPubKeyResponse\x12\x34\n\x07pub_key\x18\x01 \x01(\x0b\x32\x1d.canine_chain.filetree.PubkeyB\x04\xc8\xde\x1f\x00\"M\n\x0fQueryAllPubKeys\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8c\x01\n\x17QueryAllPubKeysResponse\x12\x34\n\x07pub_key\x18\x01 \x03(\x0b\x32\x1d.canine_chain.filetree.PubkeyB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xe0\x05\n\x05Query\x12\x80\x01\n\x06Params\x12\".canine_chain.filetree.QueryParams\x1a*.canine_chain.filetree.QueryParamsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/jackal/canine/filetree/params\x12\x99\x01\n\x04\x46ile\x12 .canine_chain.filetree.QueryFile\x1a(.canine_chain.filetree.QueryFileResponse\"E\x82\xd3\xe4\x93\x02?\x12=/jackal/canine-chain/filetree/files/{address}/{owner_address}\x12\x8b\x01\n\x08\x41llFiles\x12$.canine_chain.filetree.QueryAllFiles\x1a,.canine_chain.filetree.QueryAllFilesResponse\"+\x82\xd3\xe4\x93\x02%\x12#/jackal/canine-chain/filetree/files\x12\x92\x01\n\x06PubKey\x12\".canine_chain.filetree.QueryPubKey\x1a*.canine_chain.filetree.QueryPubKeyResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/jackal/canine-chain/filetree/pub_keys/{address}\x12\x94\x01\n\nAllPubKeys\x12&.canine_chain.filetree.QueryAllPubKeys\x1a..canine_chain.filetree.QueryAllPubKeysResponse\".\x82\xd3\xe4\x93\x02(\x12&/jackal/canine-chain/filetree/pub_keysB5Z3github.com/jackalLabs/canine-chain/x/filetree/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.filetree.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/jackalLabs/canine-chain/x/filetree/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYFILERESPONSE'].fields_by_name['file']._loaded_options = None
  _globals['_QUERYFILERESPONSE'].fields_by_name['file']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLFILESRESPONSE'].fields_by_name['files']._loaded_options = None
  _globals['_QUERYALLFILESRESPONSE'].fields_by_name['files']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPUBKEYRESPONSE'].fields_by_name['pub_key']._loaded_options = None
  _globals['_QUERYPUBKEYRESPONSE'].fields_by_name['pub_key']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLPUBKEYSRESPONSE'].fields_by_name['pub_key']._loaded_options = None
  _globals['_QUERYALLPUBKEYSRESPONSE'].fields_by_name['pub_key']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002 \022\036/jackal/canine/filetree/params'
  _globals['_QUERY'].methods_by_name['File']._loaded_options = None
  _globals['_QUERY'].methods_by_name['File']._serialized_options = b'\202\323\344\223\002?\022=/jackal/canine-chain/filetree/files/{address}/{owner_address}'
  _globals['_QUERY'].methods_by_name['AllFiles']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllFiles']._serialized_options = b'\202\323\344\223\002%\022#/jackal/canine-chain/filetree/files'
  _globals['_QUERY'].methods_by_name['PubKey']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PubKey']._serialized_options = b'\202\323\344\223\0022\0220/jackal/canine-chain/filetree/pub_keys/{address}'
  _globals['_QUERY'].methods_by_name['AllPubKeys']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllPubKeys']._serialized_options = b'\202\323\344\223\002(\022&/jackal/canine-chain/filetree/pub_keys'
  _globals['_QUERYPARAMS']._serialized_start=263
  _globals['_QUERYPARAMS']._serialized_end=276
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=278
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=352
  _globals['_QUERYFILE']._serialized_start=354
  _globals['_QUERYFILE']._serialized_end=405
  _globals['_QUERYFILERESPONSE']._serialized_start=407
  _globals['_QUERYFILERESPONSE']._serialized_end=476
  _globals['_QUERYALLFILES']._serialized_start=478
  _globals['_QUERYALLFILES']._serialized_end=553
  _globals['_QUERYALLFILESRESPONSE']._serialized_start=556
  _globals['_QUERYALLFILESRESPONSE']._serialized_end=691
  _globals['_QUERYPUBKEY']._serialized_start=693
  _globals['_QUERYPUBKEY']._serialized_end=723
  _globals['_QUERYPUBKEYRESPONSE']._serialized_start=725
  _globals['_QUERYPUBKEYRESPONSE']._serialized_end=800
  _globals['_QUERYALLPUBKEYS']._serialized_start=802
  _globals['_QUERYALLPUBKEYS']._serialized_end=879
  _globals['_QUERYALLPUBKEYSRESPONSE']._serialized_start=882
  _globals['_QUERYALLPUBKEYSRESPONSE']._serialized_end=1022
  _globals['_QUERY']._serialized_start=1025
  _globals['_QUERY']._serialized_end=1761
# @@protoc_insertion_point(module_scope)
