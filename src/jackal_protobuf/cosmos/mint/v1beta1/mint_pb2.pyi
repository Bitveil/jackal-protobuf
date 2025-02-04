
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Minter(_message.Message):
    __slots__ = ['annual_provisions', 'inflation']
    ANNUAL_PROVISIONS_FIELD_NUMBER: _ClassVar[int]
    INFLATION_FIELD_NUMBER: _ClassVar[int]
    annual_provisions: str
    inflation: str

    def __init__(self, inflation: _Optional[str]=..., annual_provisions: _Optional[str]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ['blocks_per_year', 'goal_bonded', 'inflation_max', 'inflation_min', 'inflation_rate_change', 'mint_denom']
    BLOCKS_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
    GOAL_BONDED_FIELD_NUMBER: _ClassVar[int]
    INFLATION_MAX_FIELD_NUMBER: _ClassVar[int]
    INFLATION_MIN_FIELD_NUMBER: _ClassVar[int]
    INFLATION_RATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MINT_DENOM_FIELD_NUMBER: _ClassVar[int]
    blocks_per_year: int
    goal_bonded: str
    inflation_max: str
    inflation_min: str
    inflation_rate_change: str
    mint_denom: str

    def __init__(self, mint_denom: _Optional[str]=..., inflation_rate_change: _Optional[str]=..., inflation_max: _Optional[str]=..., inflation_min: _Optional[str]=..., goal_bonded: _Optional[str]=..., blocks_per_year: _Optional[int]=...) -> None:
        ...
