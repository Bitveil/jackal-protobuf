
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.gov.v1beta1 import gov_pb2 as _gov_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryDepositRequest(_message.Message):
    __slots__ = ['depositor', 'proposal_id']
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    depositor: str
    proposal_id: int

    def __init__(self, proposal_id: _Optional[int]=..., depositor: _Optional[str]=...) -> None:
        ...

class QueryDepositResponse(_message.Message):
    __slots__ = ['deposit']
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    deposit: _gov_pb2.Deposit

    def __init__(self, deposit: _Optional[_Union[(_gov_pb2.Deposit, _Mapping)]]=...) -> None:
        ...

class QueryDepositsRequest(_message.Message):
    __slots__ = ['pagination', 'proposal_id']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    proposal_id: int

    def __init__(self, proposal_id: _Optional[int]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class QueryDepositsResponse(_message.Message):
    __slots__ = ['deposits', 'pagination']
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    deposits: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Deposit]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, deposits: _Optional[_Iterable[_Union[(_gov_pb2.Deposit, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class QueryParamsRequest(_message.Message):
    __slots__ = ['params_type']
    PARAMS_TYPE_FIELD_NUMBER: _ClassVar[int]
    params_type: str

    def __init__(self, params_type: _Optional[str]=...) -> None:
        ...

class QueryParamsResponse(_message.Message):
    __slots__ = ['deposit_params', 'tally_params', 'voting_params']
    DEPOSIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TALLY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VOTING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deposit_params: _gov_pb2.DepositParams
    tally_params: _gov_pb2.TallyParams
    voting_params: _gov_pb2.VotingParams

    def __init__(self, voting_params: _Optional[_Union[(_gov_pb2.VotingParams, _Mapping)]]=..., deposit_params: _Optional[_Union[(_gov_pb2.DepositParams, _Mapping)]]=..., tally_params: _Optional[_Union[(_gov_pb2.TallyParams, _Mapping)]]=...) -> None:
        ...

class QueryProposalRequest(_message.Message):
    __slots__ = ['proposal_id']
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int

    def __init__(self, proposal_id: _Optional[int]=...) -> None:
        ...

class QueryProposalResponse(_message.Message):
    __slots__ = ['proposal']
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: _gov_pb2.Proposal

    def __init__(self, proposal: _Optional[_Union[(_gov_pb2.Proposal, _Mapping)]]=...) -> None:
        ...

class QueryProposalsRequest(_message.Message):
    __slots__ = ['depositor', 'pagination', 'proposal_status', 'voter']
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    depositor: str
    pagination: _pagination_pb2.PageRequest
    proposal_status: _gov_pb2.ProposalStatus
    voter: str

    def __init__(self, proposal_status: _Optional[_Union[(_gov_pb2.ProposalStatus, str)]]=..., voter: _Optional[str]=..., depositor: _Optional[str]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class QueryProposalsResponse(_message.Message):
    __slots__ = ['pagination', 'proposals']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageResponse
    proposals: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Proposal]

    def __init__(self, proposals: _Optional[_Iterable[_Union[(_gov_pb2.Proposal, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class QueryTallyResultRequest(_message.Message):
    __slots__ = ['proposal_id']
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int

    def __init__(self, proposal_id: _Optional[int]=...) -> None:
        ...

class QueryTallyResultResponse(_message.Message):
    __slots__ = ['tally']
    TALLY_FIELD_NUMBER: _ClassVar[int]
    tally: _gov_pb2.TallyResult

    def __init__(self, tally: _Optional[_Union[(_gov_pb2.TallyResult, _Mapping)]]=...) -> None:
        ...

class QueryVoteRequest(_message.Message):
    __slots__ = ['proposal_id', 'voter']
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTER_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    voter: str

    def __init__(self, proposal_id: _Optional[int]=..., voter: _Optional[str]=...) -> None:
        ...

class QueryVoteResponse(_message.Message):
    __slots__ = ['vote']
    VOTE_FIELD_NUMBER: _ClassVar[int]
    vote: _gov_pb2.Vote

    def __init__(self, vote: _Optional[_Union[(_gov_pb2.Vote, _Mapping)]]=...) -> None:
        ...

class QueryVotesRequest(_message.Message):
    __slots__ = ['pagination', 'proposal_id']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    proposal_id: int

    def __init__(self, proposal_id: _Optional[int]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class QueryVotesResponse(_message.Message):
    __slots__ = ['pagination', 'votes']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageResponse
    votes: _containers.RepeatedCompositeFieldContainer[_gov_pb2.Vote]

    def __init__(self, votes: _Optional[_Iterable[_Union[(_gov_pb2.Vote, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...
