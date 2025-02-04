
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/distribution/v1beta1/tx.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x91\x01\n\x15MsgSetWithdrawAddress\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x125\n\x10withdraw_address\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"withdraw_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1f\n\x1dMsgSetWithdrawAddressResponse"\x98\x01\n\x1aMsgWithdrawDelegatorReward\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"$\n"MsgWithdrawDelegatorRewardResponse"c\n\x1eMsgWithdrawValidatorCommission\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"(\n&MsgWithdrawValidatorCommissionResponse"\x90\x01\n\x14MsgFundCommunityPool\x12[\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x11\n\tdepositor\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1e\n\x1cMsgFundCommunityPoolResponse2\xc8\x04\n\x03Msg\x12\x84\x01\n\x12SetWithdrawAddress\x122.cosmos.distribution.v1beta1.MsgSetWithdrawAddress\x1a:.cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse\x12\x93\x01\n\x17WithdrawDelegatorReward\x127.cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward\x1a?.cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse\x12\x9f\x01\n\x1bWithdrawValidatorCommission\x12;.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission\x1aC.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse\x12\x81\x01\n\x11FundCommunityPool\x121.cosmos.distribution.v1beta1.MsgFundCommunityPool\x1a9.cosmos.distribution.v1beta1.MsgFundCommunityPoolResponseB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.tx_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _MSGSETWITHDRAWADDRESS.fields_by_name['delegator_address']._options = None
    _MSGSETWITHDRAWADDRESS.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGSETWITHDRAWADDRESS.fields_by_name['withdraw_address']._options = None
    _MSGSETWITHDRAWADDRESS.fields_by_name['withdraw_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"withdraw_address"'
    _MSGSETWITHDRAWADDRESS._options = None
    _MSGSETWITHDRAWADDRESS._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGWITHDRAWDELEGATORREWARD.fields_by_name['delegator_address']._options = None
    _MSGWITHDRAWDELEGATORREWARD.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGWITHDRAWDELEGATORREWARD.fields_by_name['validator_address']._options = None
    _MSGWITHDRAWDELEGATORREWARD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _MSGWITHDRAWDELEGATORREWARD._options = None
    _MSGWITHDRAWDELEGATORREWARD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGWITHDRAWVALIDATORCOMMISSION.fields_by_name['validator_address']._options = None
    _MSGWITHDRAWVALIDATORCOMMISSION.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _MSGWITHDRAWVALIDATORCOMMISSION._options = None
    _MSGWITHDRAWVALIDATORCOMMISSION._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGFUNDCOMMUNITYPOOL.fields_by_name['amount']._options = None
    _MSGFUNDCOMMUNITYPOOL.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGFUNDCOMMUNITYPOOL._options = None
    _MSGFUNDCOMMUNITYPOOL._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGSETWITHDRAWADDRESS._serialized_start = 124
    _MSGSETWITHDRAWADDRESS._serialized_end = 269
    _MSGSETWITHDRAWADDRESSRESPONSE._serialized_start = 271
    _MSGSETWITHDRAWADDRESSRESPONSE._serialized_end = 302
    _MSGWITHDRAWDELEGATORREWARD._serialized_start = 305
    _MSGWITHDRAWDELEGATORREWARD._serialized_end = 457
    _MSGWITHDRAWDELEGATORREWARDRESPONSE._serialized_start = 459
    _MSGWITHDRAWDELEGATORREWARDRESPONSE._serialized_end = 495
    _MSGWITHDRAWVALIDATORCOMMISSION._serialized_start = 497
    _MSGWITHDRAWVALIDATORCOMMISSION._serialized_end = 596
    _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE._serialized_start = 598
    _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE._serialized_end = 638
    _MSGFUNDCOMMUNITYPOOL._serialized_start = 641
    _MSGFUNDCOMMUNITYPOOL._serialized_end = 785
    _MSGFUNDCOMMUNITYPOOLRESPONSE._serialized_start = 787
    _MSGFUNDCOMMUNITYPOOLRESPONSE._serialized_end = 817
    _MSG._serialized_start = 820
    _MSG._serialized_end = 1404
