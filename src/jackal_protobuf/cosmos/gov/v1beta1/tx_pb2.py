
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/gov/v1beta1/tx.proto\x12\x12cosmos.gov.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ccosmos/gov/v1beta1/gov.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xeb\x01\n\x11MsgSubmitProposal\x122\n\x07content\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07Content\x12~\n\x0finitial_deposit\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBJ\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x16yaml:"initial_deposit"\x12\x10\n\x08proposer\x18\x03 \x01(\t:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"W\n\x19MsgSubmitProposalResponse\x12:\n\x0bproposal_id\x18\x01 \x01(\x04B%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id""\x96\x01\n\x07MsgVote\x12:\n\x0bproposal_id\x18\x01 \x01(\x04B%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"\x12\r\n\x05voter\x18\x02 \x01(\t\x12.\n\x06option\x18\x03 \x01(\x0e2\x1e.cosmos.gov.v1beta1.VoteOption:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x11\n\x0fMsgVoteResponse"\x9e\x01\n\x0fMsgVoteWeighted\x12+\n\x0bproposal_id\x18\x01 \x01(\x04B\x16\xf2\xde\x1f\x12yaml:"proposal_id"\x12\r\n\x05voter\x18\x02 \x01(\t\x12=\n\x07options\x18\x03 \x03(\x0b2&.cosmos.gov.v1beta1.WeightedVoteOptionB\x04\xc8\xde\x1f\x00:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x19\n\x17MsgVoteWeightedResponse"\xca\x01\n\nMsgDeposit\x12:\n\x0bproposal_id\x18\x01 \x01(\x04B%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"\x12\x11\n\tdepositor\x18\x02 \x01(\t\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x14\n\x12MsgDepositResponse2\xec\x02\n\x03Msg\x12f\n\x0eSubmitProposal\x12%.cosmos.gov.v1beta1.MsgSubmitProposal\x1a-.cosmos.gov.v1beta1.MsgSubmitProposalResponse\x12H\n\x04Vote\x12\x1b.cosmos.gov.v1beta1.MsgVote\x1a#.cosmos.gov.v1beta1.MsgVoteResponse\x12`\n\x0cVoteWeighted\x12#.cosmos.gov.v1beta1.MsgVoteWeighted\x1a+.cosmos.gov.v1beta1.MsgVoteWeightedResponse\x12Q\n\x07Deposit\x12\x1e.cosmos.gov.v1beta1.MsgDeposit\x1a&.cosmos.gov.v1beta1.MsgDepositResponseB*Z(github.com/cosmos/cosmos-sdk/x/gov/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.tx_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/x/gov/types'
    _MSGSUBMITPROPOSAL.fields_by_name['content']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['content']._serialized_options = b'\xca\xb4-\x07Content'
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x16yaml:"initial_deposit"'
    _MSGSUBMITPROPOSAL._options = None
    _MSGSUBMITPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00'
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name['proposal_id']._options = None
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"'
    _MSGVOTE.fields_by_name['proposal_id']._options = None
    _MSGVOTE.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"'
    _MSGVOTE._options = None
    _MSGVOTE._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00'
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._serialized_options = b'\xf2\xde\x1f\x12yaml:"proposal_id"'
    _MSGVOTEWEIGHTED.fields_by_name['options']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['options']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGVOTEWEIGHTED._options = None
    _MSGVOTEWEIGHTED._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00'
    _MSGDEPOSIT.fields_by_name['proposal_id']._options = None
    _MSGDEPOSIT.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"'
    _MSGDEPOSIT.fields_by_name['amount']._options = None
    _MSGDEPOSIT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGDEPOSIT._options = None
    _MSGDEPOSIT._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00'
    _MSGSUBMITPROPOSAL._serialized_start = 190
    _MSGSUBMITPROPOSAL._serialized_end = 425
    _MSGSUBMITPROPOSALRESPONSE._serialized_start = 427
    _MSGSUBMITPROPOSALRESPONSE._serialized_end = 514
    _MSGVOTE._serialized_start = 517
    _MSGVOTE._serialized_end = 667
    _MSGVOTERESPONSE._serialized_start = 669
    _MSGVOTERESPONSE._serialized_end = 686
    _MSGVOTEWEIGHTED._serialized_start = 689
    _MSGVOTEWEIGHTED._serialized_end = 847
    _MSGVOTEWEIGHTEDRESPONSE._serialized_start = 849
    _MSGVOTEWEIGHTEDRESPONSE._serialized_end = 874
    _MSGDEPOSIT._serialized_start = 877
    _MSGDEPOSIT._serialized_end = 1079
    _MSGDEPOSITRESPONSE._serialized_start = 1081
    _MSGDEPOSITRESPONSE._serialized_end = 1101
    _MSG._serialized_start = 1104
    _MSG._serialized_end = 1468
