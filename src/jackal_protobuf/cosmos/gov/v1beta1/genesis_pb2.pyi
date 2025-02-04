
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.gov.v1beta1 import gov_pb2 as _gov_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['deposit_params', 'deposits', 'proposals', 'starting_proposal_id', 'tally_params', 'votes', 'voting_params']
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    STARTING_PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    TALLY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    VOTING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deposit_params: _gov_pb2.DepositParams
    deposits: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Deposit]
    proposals: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Proposal]
    starting_proposal_id: int
    tally_params: _gov_pb2.TallyParams
    votes: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Vote]
    voting_params: _gov_pb2.VotingParams

    def __init__(self, starting_proposal_id: _Optional[int]=..., deposits: _Optional[_Iterable[_Union[(_gov_pb2.Deposit, _Mapping)]]]=..., votes: _Optional[_Iterable[_Union[(_gov_pb2.Vote, _Mapping)]]]=..., proposals: _Optional[_Iterable[_Union[(_gov_pb2.Proposal, _Mapping)]]]=..., deposit_params: _Optional[_Union[(_gov_pb2.DepositParams, _Mapping)]]=..., voting_params: _Optional[_Union[(_gov_pb2.VotingParams, _Mapping)]]=..., tally_params: _Optional[_Union[(_gov_pb2.TallyParams, _Mapping)]]=...) -> None:
        ...
