"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63\x61nine_chain/filetree/tx.proto\x12\x15\x63\x61nine_chain.filetree\"\xa5\x01\n\x0bMsgPostFile\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\t\x12\x13\n\x0bhash_parent\x18\x03 \x01(\t\x12\x12\n\nhash_child\x18\x04 \x01(\t\x12\x10\n\x08\x63ontents\x18\x05 \x01(\t\x12\x0f\n\x07viewers\x18\x06 \x01(\t\x12\x0f\n\x07\x65\x64itors\x18\x07 \x01(\t\x12\x17\n\x0ftracking_number\x18\x08 \x01(\t\"#\n\x13MsgPostFileResponse\x12\x0c\n\x04path\x18\x01 \x01(\t\"n\n\rMsgAddViewers\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x12\n\nviewer_ids\x18\x02 \x01(\t\x12\x13\n\x0bviewer_keys\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x12\n\nfile_owner\x18\x05 \x01(\t\"\x17\n\x15MsgAddViewersResponse\"*\n\nMsgPostKey\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x14\n\x12MsgPostKeyResponse\"D\n\rMsgDeleteFile\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x11\n\thash_path\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\t\"\x17\n\x15MsgDeleteFileResponse\"\\\n\x10MsgRemoveViewers\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x12\n\nviewer_ids\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x12\n\nfile_owner\x18\x04 \x01(\t\"\x1a\n\x18MsgRemoveViewersResponse\"b\n\x14MsgProvisionFileTree\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07\x65\x64itors\x18\x02 \x01(\t\x12\x0f\n\x07viewers\x18\x03 \x01(\t\x12\x17\n\x0ftracking_number\x18\x04 \x01(\t\"\x1e\n\x1cMsgProvisionFileTreeResponse\"n\n\rMsgAddEditors\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x12\n\neditor_ids\x18\x02 \x01(\t\x12\x13\n\x0b\x65\x64itor_keys\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x12\n\nfile_owner\x18\x05 \x01(\t\"\x17\n\x15MsgAddEditorsResponse\"\\\n\x10MsgRemoveEditors\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x12\n\neditor_ids\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x12\n\nfile_owner\x18\x04 \x01(\t\"\x1a\n\x18MsgRemoveEditorsResponse\"G\n\x0fMsgResetEditors\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x12\n\nfile_owner\x18\x03 \x01(\t\"\x19\n\x17MsgResetEditorsResponse\"G\n\x0fMsgResetViewers\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x12\n\nfile_owner\x18\x03 \x01(\t\"\x19\n\x17MsgResetViewersResponse\"Y\n\x0eMsgChangeOwner\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x12\n\nfile_owner\x18\x03 \x01(\t\x12\x11\n\tnew_owner\x18\x04 \x01(\t\"\x18\n\x16MsgChangeOwnerResponse2\xe2\x08\n\x03Msg\x12Z\n\x08PostFile\x12\".canine_chain.filetree.MsgPostFile\x1a*.canine_chain.filetree.MsgPostFileResponse\x12`\n\nAddViewers\x12$.canine_chain.filetree.MsgAddViewers\x1a,.canine_chain.filetree.MsgAddViewersResponse\x12W\n\x07PostKey\x12!.canine_chain.filetree.MsgPostKey\x1a).canine_chain.filetree.MsgPostKeyResponse\x12`\n\nDeleteFile\x12$.canine_chain.filetree.MsgDeleteFile\x1a,.canine_chain.filetree.MsgDeleteFileResponse\x12i\n\rRemoveViewers\x12\'.canine_chain.filetree.MsgRemoveViewers\x1a/.canine_chain.filetree.MsgRemoveViewersResponse\x12u\n\x11ProvisionFileTree\x12+.canine_chain.filetree.MsgProvisionFileTree\x1a\x33.canine_chain.filetree.MsgProvisionFileTreeResponse\x12`\n\nAddEditors\x12$.canine_chain.filetree.MsgAddEditors\x1a,.canine_chain.filetree.MsgAddEditorsResponse\x12i\n\rRemoveEditors\x12\'.canine_chain.filetree.MsgRemoveEditors\x1a/.canine_chain.filetree.MsgRemoveEditorsResponse\x12\x66\n\x0cResetEditors\x12&.canine_chain.filetree.MsgResetEditors\x1a..canine_chain.filetree.MsgResetEditorsResponse\x12\x66\n\x0cResetViewers\x12&.canine_chain.filetree.MsgResetViewers\x1a..canine_chain.filetree.MsgResetViewersResponse\x12\x63\n\x0b\x43hangeOwner\x12%.canine_chain.filetree.MsgChangeOwner\x1a-.canine_chain.filetree.MsgChangeOwnerResponseB5Z3github.com/jackalLabs/canine-chain/x/filetree/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.filetree.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/jackalLabs/canine-chain/x/filetree/types'
  _globals['_MSGPOSTFILE']._serialized_start=58
  _globals['_MSGPOSTFILE']._serialized_end=223
  _globals['_MSGPOSTFILERESPONSE']._serialized_start=225
  _globals['_MSGPOSTFILERESPONSE']._serialized_end=260
  _globals['_MSGADDVIEWERS']._serialized_start=262
  _globals['_MSGADDVIEWERS']._serialized_end=372
  _globals['_MSGADDVIEWERSRESPONSE']._serialized_start=374
  _globals['_MSGADDVIEWERSRESPONSE']._serialized_end=397
  _globals['_MSGPOSTKEY']._serialized_start=399
  _globals['_MSGPOSTKEY']._serialized_end=441
  _globals['_MSGPOSTKEYRESPONSE']._serialized_start=443
  _globals['_MSGPOSTKEYRESPONSE']._serialized_end=463
  _globals['_MSGDELETEFILE']._serialized_start=465
  _globals['_MSGDELETEFILE']._serialized_end=533
  _globals['_MSGDELETEFILERESPONSE']._serialized_start=535
  _globals['_MSGDELETEFILERESPONSE']._serialized_end=558
  _globals['_MSGREMOVEVIEWERS']._serialized_start=560
  _globals['_MSGREMOVEVIEWERS']._serialized_end=652
  _globals['_MSGREMOVEVIEWERSRESPONSE']._serialized_start=654
  _globals['_MSGREMOVEVIEWERSRESPONSE']._serialized_end=680
  _globals['_MSGPROVISIONFILETREE']._serialized_start=682
  _globals['_MSGPROVISIONFILETREE']._serialized_end=780
  _globals['_MSGPROVISIONFILETREERESPONSE']._serialized_start=782
  _globals['_MSGPROVISIONFILETREERESPONSE']._serialized_end=812
  _globals['_MSGADDEDITORS']._serialized_start=814
  _globals['_MSGADDEDITORS']._serialized_end=924
  _globals['_MSGADDEDITORSRESPONSE']._serialized_start=926
  _globals['_MSGADDEDITORSRESPONSE']._serialized_end=949
  _globals['_MSGREMOVEEDITORS']._serialized_start=951
  _globals['_MSGREMOVEEDITORS']._serialized_end=1043
  _globals['_MSGREMOVEEDITORSRESPONSE']._serialized_start=1045
  _globals['_MSGREMOVEEDITORSRESPONSE']._serialized_end=1071
  _globals['_MSGRESETEDITORS']._serialized_start=1073
  _globals['_MSGRESETEDITORS']._serialized_end=1144
  _globals['_MSGRESETEDITORSRESPONSE']._serialized_start=1146
  _globals['_MSGRESETEDITORSRESPONSE']._serialized_end=1171
  _globals['_MSGRESETVIEWERS']._serialized_start=1173
  _globals['_MSGRESETVIEWERS']._serialized_end=1244
  _globals['_MSGRESETVIEWERSRESPONSE']._serialized_start=1246
  _globals['_MSGRESETVIEWERSRESPONSE']._serialized_end=1271
  _globals['_MSGCHANGEOWNER']._serialized_start=1273
  _globals['_MSGCHANGEOWNER']._serialized_end=1362
  _globals['_MSGCHANGEOWNERRESPONSE']._serialized_start=1364
  _globals['_MSGCHANGEOWNERRESPONSE']._serialized_end=1388
  _globals['_MSG']._serialized_start=1391
  _globals['_MSG']._serialized_end=2513
# @@protoc_insertion_point(module_scope)
