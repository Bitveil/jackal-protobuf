"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63\x61nine_chain/storage/tx.proto\x12\x14\x63\x61nine_chain.storage\"\xa0\x01\n\x0bMsgPostFile\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06merkle\x18\x02 \x01(\x0c\x12\x11\n\tfile_size\x18\x03 \x01(\x03\x12\x16\n\x0eproof_interval\x18\x04 \x01(\x03\x12\x12\n\nproof_type\x18\x05 \x01(\x03\x12\x12\n\nmax_proofs\x18\x06 \x01(\x03\x12\x0f\n\x07\x65xpires\x18\x07 \x01(\x03\x12\x0c\n\x04note\x18\x08 \x01(\t\"@\n\x13MsgPostFileResponse\x12\x14\n\x0cprovider_ips\x18\x01 \x03(\t\x12\x13\n\x0bstart_block\x18\x02 \x01(\x03\"\x80\x01\n\x0cMsgPostProof\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0c\n\x04item\x18\x02 \x01(\x0c\x12\x11\n\thash_list\x18\x03 \x01(\x0c\x12\x0e\n\x06merkle\x18\x04 \x01(\x0c\x12\r\n\x05owner\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x03\x12\x10\n\x08to_prove\x18\x07 \x01(\x03\">\n\x14MsgPostProofResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"?\n\rMsgDeleteFile\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06merkle\x18\x02 \x01(\x0c\x12\r\n\x05start\x18\x03 \x01(\x03\"\x17\n\x15MsgDeleteFileResponse\"/\n\x10MsgSetProviderIP\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\"\x1a\n\x18MsgSetProviderIPResponse\"9\n\x15MsgSetProviderKeybase\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07keybase\x18\x02 \x01(\t\"\x1f\n\x1dMsgSetProviderKeybaseResponse\":\n\x18MsgSetProviderTotalSpace\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\r\n\x05space\x18\x02 \x01(\x03\"\"\n MsgSetProviderTotalSpaceResponse\"7\n\rMsgAddClaimer\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x15\n\rclaim_address\x18\x02 \x01(\t\"\x17\n\x15MsgAddClaimerResponse\":\n\x10MsgRemoveClaimer\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x15\n\rclaim_address\x18\x02 \x01(\t\"\x1a\n\x18MsgRemoveClaimerResponse\"T\n\x0fMsgInitProvider\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0f\n\x07keybase\x18\x03 \x01(\t\x12\x13\n\x0btotal_space\x18\x04 \x01(\x03\"\x19\n\x17MsgInitProviderResponse\"&\n\x13MsgShutdownProvider\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\"\x1d\n\x1bMsgShutdownProviderResponse\"\x84\x01\n\rMsgBuyStorage\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x13\n\x0b\x66or_address\x18\x02 \x01(\t\x12\x15\n\rduration_days\x18\x03 \x01(\x03\x12\r\n\x05\x62ytes\x18\x04 \x01(\x03\x12\x15\n\rpayment_denom\x18\x05 \x01(\t\x12\x10\n\x08referral\x18\x06 \x01(\t\"\x17\n\x15MsgBuyStorageResponse\"Z\n\x19MsgRequestAttestationForm\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06merkle\x18\x02 \x01(\x0c\x12\r\n\x05owner\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\"V\n!MsgRequestAttestationFormResponse\x12\x11\n\tproviders\x18\x01 \x03(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"Z\n\tMsgAttest\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06prover\x18\x02 \x01(\t\x12\x0e\n\x06merkle\x18\x03 \x01(\x0c\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\"\x13\n\x11MsgAttestResponse\"e\n\x14MsgRequestReportForm\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06prover\x18\x02 \x01(\t\x12\x0e\n\x06merkle\x18\x03 \x01(\x0c\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\"Q\n\x1cMsgRequestReportFormResponse\x12\x11\n\tproviders\x18\x01 \x03(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"Z\n\tMsgReport\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0e\n\x06prover\x18\x02 \x01(\t\x12\x0e\n\x06merkle\x18\x03 \x01(\x0c\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\"\x13\n\x11MsgReportResponse2\xb1\x0c\n\x03Msg\x12X\n\x08PostFile\x12!.canine_chain.storage.MsgPostFile\x1a).canine_chain.storage.MsgPostFileResponse\x12[\n\tPostProof\x12\".canine_chain.storage.MsgPostProof\x1a*.canine_chain.storage.MsgPostProofResponse\x12^\n\nDeleteFile\x12#.canine_chain.storage.MsgDeleteFile\x1a+.canine_chain.storage.MsgDeleteFileResponse\x12g\n\rSetProviderIP\x12&.canine_chain.storage.MsgSetProviderIP\x1a..canine_chain.storage.MsgSetProviderIPResponse\x12v\n\x12SetProviderKeybase\x12+.canine_chain.storage.MsgSetProviderKeybase\x1a\x33.canine_chain.storage.MsgSetProviderKeybaseResponse\x12\x7f\n\x15SetProviderTotalSpace\x12..canine_chain.storage.MsgSetProviderTotalSpace\x1a\x36.canine_chain.storage.MsgSetProviderTotalSpaceResponse\x12\x64\n\x0cInitProvider\x12%.canine_chain.storage.MsgInitProvider\x1a-.canine_chain.storage.MsgInitProviderResponse\x12p\n\x10ShutdownProvider\x12).canine_chain.storage.MsgShutdownProvider\x1a\x31.canine_chain.storage.MsgShutdownProviderResponse\x12^\n\nBuyStorage\x12#.canine_chain.storage.MsgBuyStorage\x1a+.canine_chain.storage.MsgBuyStorageResponse\x12\x66\n\x12\x41\x64\x64ProviderClaimer\x12#.canine_chain.storage.MsgAddClaimer\x1a+.canine_chain.storage.MsgAddClaimerResponse\x12o\n\x15RemoveProviderClaimer\x12&.canine_chain.storage.MsgRemoveClaimer\x1a..canine_chain.storage.MsgRemoveClaimerResponse\x12\x82\x01\n\x16RequestAttestationForm\x12/.canine_chain.storage.MsgRequestAttestationForm\x1a\x37.canine_chain.storage.MsgRequestAttestationFormResponse\x12R\n\x06\x41ttest\x12\x1f.canine_chain.storage.MsgAttest\x1a\'.canine_chain.storage.MsgAttestResponse\x12s\n\x11RequestReportForm\x12*.canine_chain.storage.MsgRequestReportForm\x1a\x32.canine_chain.storage.MsgRequestReportFormResponse\x12R\n\x06Report\x12\x1f.canine_chain.storage.MsgReport\x1a\'.canine_chain.storage.MsgReportResponseB4Z2github.com/jackalLabs/canine-chain/x/storage/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.storage.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/jackalLabs/canine-chain/x/storage/types'
  _globals['_MSGPOSTFILE']._serialized_start=56
  _globals['_MSGPOSTFILE']._serialized_end=216
  _globals['_MSGPOSTFILERESPONSE']._serialized_start=218
  _globals['_MSGPOSTFILERESPONSE']._serialized_end=282
  _globals['_MSGPOSTPROOF']._serialized_start=285
  _globals['_MSGPOSTPROOF']._serialized_end=413
  _globals['_MSGPOSTPROOFRESPONSE']._serialized_start=415
  _globals['_MSGPOSTPROOFRESPONSE']._serialized_end=477
  _globals['_MSGDELETEFILE']._serialized_start=479
  _globals['_MSGDELETEFILE']._serialized_end=542
  _globals['_MSGDELETEFILERESPONSE']._serialized_start=544
  _globals['_MSGDELETEFILERESPONSE']._serialized_end=567
  _globals['_MSGSETPROVIDERIP']._serialized_start=569
  _globals['_MSGSETPROVIDERIP']._serialized_end=616
  _globals['_MSGSETPROVIDERIPRESPONSE']._serialized_start=618
  _globals['_MSGSETPROVIDERIPRESPONSE']._serialized_end=644
  _globals['_MSGSETPROVIDERKEYBASE']._serialized_start=646
  _globals['_MSGSETPROVIDERKEYBASE']._serialized_end=703
  _globals['_MSGSETPROVIDERKEYBASERESPONSE']._serialized_start=705
  _globals['_MSGSETPROVIDERKEYBASERESPONSE']._serialized_end=736
  _globals['_MSGSETPROVIDERTOTALSPACE']._serialized_start=738
  _globals['_MSGSETPROVIDERTOTALSPACE']._serialized_end=796
  _globals['_MSGSETPROVIDERTOTALSPACERESPONSE']._serialized_start=798
  _globals['_MSGSETPROVIDERTOTALSPACERESPONSE']._serialized_end=832
  _globals['_MSGADDCLAIMER']._serialized_start=834
  _globals['_MSGADDCLAIMER']._serialized_end=889
  _globals['_MSGADDCLAIMERRESPONSE']._serialized_start=891
  _globals['_MSGADDCLAIMERRESPONSE']._serialized_end=914
  _globals['_MSGREMOVECLAIMER']._serialized_start=916
  _globals['_MSGREMOVECLAIMER']._serialized_end=974
  _globals['_MSGREMOVECLAIMERRESPONSE']._serialized_start=976
  _globals['_MSGREMOVECLAIMERRESPONSE']._serialized_end=1002
  _globals['_MSGINITPROVIDER']._serialized_start=1004
  _globals['_MSGINITPROVIDER']._serialized_end=1088
  _globals['_MSGINITPROVIDERRESPONSE']._serialized_start=1090
  _globals['_MSGINITPROVIDERRESPONSE']._serialized_end=1115
  _globals['_MSGSHUTDOWNPROVIDER']._serialized_start=1117
  _globals['_MSGSHUTDOWNPROVIDER']._serialized_end=1155
  _globals['_MSGSHUTDOWNPROVIDERRESPONSE']._serialized_start=1157
  _globals['_MSGSHUTDOWNPROVIDERRESPONSE']._serialized_end=1186
  _globals['_MSGBUYSTORAGE']._serialized_start=1189
  _globals['_MSGBUYSTORAGE']._serialized_end=1321
  _globals['_MSGBUYSTORAGERESPONSE']._serialized_start=1323
  _globals['_MSGBUYSTORAGERESPONSE']._serialized_end=1346
  _globals['_MSGREQUESTATTESTATIONFORM']._serialized_start=1348
  _globals['_MSGREQUESTATTESTATIONFORM']._serialized_end=1438
  _globals['_MSGREQUESTATTESTATIONFORMRESPONSE']._serialized_start=1440
  _globals['_MSGREQUESTATTESTATIONFORMRESPONSE']._serialized_end=1526
  _globals['_MSGATTEST']._serialized_start=1528
  _globals['_MSGATTEST']._serialized_end=1618
  _globals['_MSGATTESTRESPONSE']._serialized_start=1620
  _globals['_MSGATTESTRESPONSE']._serialized_end=1639
  _globals['_MSGREQUESTREPORTFORM']._serialized_start=1641
  _globals['_MSGREQUESTREPORTFORM']._serialized_end=1742
  _globals['_MSGREQUESTREPORTFORMRESPONSE']._serialized_start=1744
  _globals['_MSGREQUESTREPORTFORMRESPONSE']._serialized_end=1825
  _globals['_MSGREPORT']._serialized_start=1827
  _globals['_MSGREPORT']._serialized_end=1917
  _globals['_MSGREPORTRESPONSE']._serialized_start=1919
  _globals['_MSGREPORTRESPONSE']._serialized_end=1938
  _globals['_MSG']._serialized_start=1941
  _globals['_MSG']._serialized_end=3526
# @@protoc_insertion_point(module_scope)
