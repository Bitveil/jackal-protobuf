
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x8a\x03\n\x06Params\x12]\n\rcommunity_tax\x18\x01 \x01(\tBF\xf2\xde\x1f\x14yaml:"community_tax"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12k\n\x14base_proposer_reward\x18\x02 \x01(\tBM\xf2\xde\x1f\x1byaml:"base_proposer_reward"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12m\n\x15bonus_proposer_reward\x18\x03 \x01(\tBN\xf2\xde\x1f\x1cyaml:"bonus_proposer_reward"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12?\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08B \xf2\xde\x1f\x1cyaml:"withdraw_addr_enabled":\x04\x98\xa0\x1f\x00"\xe8\x01\n\x1aValidatorHistoricalRewards\x12\x94\x01\n\x17cumulative_reward_ratio\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinBU\xf2\xde\x1f\x1eyaml:"cumulative_reward_ratio"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x123\n\x0freference_count\x18\x02 \x01(\rB\x1a\xf2\xde\x1f\x16yaml:"reference_count""\x8d\x01\n\x17ValidatorCurrentRewards\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x0e\n\x06period\x18\x02 \x01(\x04"\x87\x01\n\x1eValidatorAccumulatedCommission\x12e\n\ncommission\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00"\x93\x01\n\x1bValidatorOutstandingRewards\x12t\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinBE\xf2\xde\x1f\x0eyaml:"rewards"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00"\x8e\x01\n\x13ValidatorSlashEvent\x125\n\x10validator_period\x18\x01 \x01(\x04B\x1b\xf2\xde\x1f\x17yaml:"validator_period"\x12@\n\x08fraction\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x95\x01\n\x14ValidatorSlashEvents\x12w\n\x16validator_slash_events\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB%\xf2\xde\x1f\x1dyaml:"validator_slash_events"\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00"\x8e\x01\n\x07FeePool\x12\x82\x01\n\x0ecommunity_pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinBL\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xf2\xde\x1f\x15yaml:"community_pool""\xbe\x01\n\x1aCommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06amount\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\xda\x01\n\x15DelegatorStartingInfo\x123\n\x0fprevious_period\x18\x01 \x01(\x04B\x1a\xf2\xde\x1f\x16yaml:"previous_period"\x12M\n\x05stake\x18\x02 \x01(\tB>\xf2\xde\x1f\x0cyaml:"stake"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x06height\x18\x03 \x01(\x04B-\xf2\xde\x1f\x16yaml:"creation_height"\xea\xde\x1f\x0fcreation_height"\xc1\x01\n\x19DelegationDelegatorReward\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12a\n\x06reward\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\xf0\x01\n%CommunityPoolSpendProposalWithDeposit\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"title"\x12+\n\x0bdescription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"description"\x12\'\n\trecipient\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"recipient"\x12!\n\x06amount\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:"amount"\x12#\n\x07deposit\x18\x05 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"deposit":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.distribution_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _PARAMS.fields_by_name['community_tax']._options = None
    _PARAMS.fields_by_name['community_tax']._serialized_options = b'\xf2\xde\x1f\x14yaml:"community_tax"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['base_proposer_reward']._options = None
    _PARAMS.fields_by_name['base_proposer_reward']._serialized_options = b'\xf2\xde\x1f\x1byaml:"base_proposer_reward"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['bonus_proposer_reward']._options = None
    _PARAMS.fields_by_name['bonus_proposer_reward']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"bonus_proposer_reward"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['withdraw_addr_enabled']._options = None
    _PARAMS.fields_by_name['withdraw_addr_enabled']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"withdraw_addr_enabled"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"cumulative_reward_ratio"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORHISTORICALREWARDS.fields_by_name['reference_count']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name['reference_count']._serialized_options = b'\xf2\xde\x1f\x16yaml:"reference_count"'
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = None
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"rewards"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENT.fields_by_name['validator_period']._options = None
    _VALIDATORSLASHEVENT.fields_by_name['validator_period']._serialized_options = b'\xf2\xde\x1f\x17yaml:"validator_period"'
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._options = None
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = None
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._serialized_options = b'\xf2\xde\x1f\x1dyaml:"validator_slash_events"\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTS._options = None
    _VALIDATORSLASHEVENTS._serialized_options = b'\x98\xa0\x1f\x00'
    _FEEPOOL.fields_by_name['community_pool']._options = None
    _FEEPOOL.fields_by_name['community_pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xf2\xde\x1f\x15yaml:"community_pool"'
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _COMMUNITYPOOLSPENDPROPOSAL._options = None
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _DELEGATORSTARTINGINFO.fields_by_name['previous_period']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['previous_period']._serialized_options = b'\xf2\xde\x1f\x16yaml:"previous_period"'
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"stake"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _DELEGATORSTARTINGINFO.fields_by_name['height']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['height']._serialized_options = b'\xf2\xde\x1f\x16yaml:"creation_height"\xea\xde\x1f\x0fcreation_height'
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _DELEGATIONDELEGATORREWARD._options = None
    _DELEGATIONDELEGATORREWARD._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"title"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._serialized_options = b'\xf2\xde\x1f\x12yaml:"description"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._serialized_options = b'\xf2\xde\x1f\x10yaml:"recipient"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"deposit"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _PARAMS._serialized_start = 134
    _PARAMS._serialized_end = 528
    _VALIDATORHISTORICALREWARDS._serialized_start = 531
    _VALIDATORHISTORICALREWARDS._serialized_end = 763
    _VALIDATORCURRENTREWARDS._serialized_start = 766
    _VALIDATORCURRENTREWARDS._serialized_end = 907
    _VALIDATORACCUMULATEDCOMMISSION._serialized_start = 910
    _VALIDATORACCUMULATEDCOMMISSION._serialized_end = 1045
    _VALIDATOROUTSTANDINGREWARDS._serialized_start = 1048
    _VALIDATOROUTSTANDINGREWARDS._serialized_end = 1195
    _VALIDATORSLASHEVENT._serialized_start = 1198
    _VALIDATORSLASHEVENT._serialized_end = 1340
    _VALIDATORSLASHEVENTS._serialized_start = 1343
    _VALIDATORSLASHEVENTS._serialized_end = 1492
    _FEEPOOL._serialized_start = 1495
    _FEEPOOL._serialized_end = 1637
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_start = 1640
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_end = 1830
    _DELEGATORSTARTINGINFO._serialized_start = 1833
    _DELEGATORSTARTINGINFO._serialized_end = 2051
    _DELEGATIONDELEGATORREWARD._serialized_start = 2054
    _DELEGATIONDELEGATORREWARD._serialized_end = 2247
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_start = 2250
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_end = 2490
