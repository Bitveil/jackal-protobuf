
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateVestingAccount(_message.Message):
    __slots__ = ['amount', 'delayed', 'end_time', 'from_address', 'to_address']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DELAYED_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    delayed: bool
    end_time: int
    from_address: str
    to_address: str

    def __init__(self, from_address: _Optional[str]=..., to_address: _Optional[str]=..., amount: _Optional[_Iterable[_Union[(_coin_pb2.Coin, _Mapping)]]]=..., end_time: _Optional[int]=..., delayed: bool=...) -> None:
        ...

class MsgCreateVestingAccountResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...
