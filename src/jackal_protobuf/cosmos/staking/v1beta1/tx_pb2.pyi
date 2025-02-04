
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.staking.v1beta1 import staking_pb2 as _staking_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgBeginRedelegate(_message.Message):
    __slots__ = ['amount', 'delegator_address', 'validator_dst_address', 'validator_src_address']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_DST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SRC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    delegator_address: str
    validator_dst_address: str
    validator_src_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_src_address: _Optional[str]=..., validator_dst_address: _Optional[str]=..., amount: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=...) -> None:
        ...

class MsgBeginRedelegateResponse(_message.Message):
    __slots__ = ['completion_time']
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    completion_time: _timestamp_pb2.Timestamp

    def __init__(self, completion_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...

class MsgCreateValidator(_message.Message):
    __slots__ = ['commission', 'delegator_address', 'description', 'min_self_delegation', 'pubkey', 'validator_address', 'value']
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIN_SELF_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    commission: _staking_pb2.CommissionRates
    delegator_address: str
    description: _staking_pb2.Description
    min_self_delegation: str
    pubkey: _any_pb2.Any
    validator_address: str
    value: _coin_pb2.Coin

    def __init__(self, description: _Optional[_Union[(_staking_pb2.Description, _Mapping)]]=..., commission: _Optional[_Union[(_staking_pb2.CommissionRates, _Mapping)]]=..., min_self_delegation: _Optional[str]=..., delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., pubkey: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., value: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=...) -> None:
        ...

class MsgCreateValidatorResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgDelegate(_message.Message):
    __slots__ = ['amount', 'delegator_address', 'validator_address']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    delegator_address: str
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., amount: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=...) -> None:
        ...

class MsgDelegateResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgEditValidator(_message.Message):
    __slots__ = ['commission_rate', 'description', 'min_self_delegation', 'validator_address']
    COMMISSION_RATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIN_SELF_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    commission_rate: str
    description: _staking_pb2.Description
    min_self_delegation: str
    validator_address: str

    def __init__(self, description: _Optional[_Union[(_staking_pb2.Description, _Mapping)]]=..., validator_address: _Optional[str]=..., commission_rate: _Optional[str]=..., min_self_delegation: _Optional[str]=...) -> None:
        ...

class MsgEditValidatorResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgUndelegate(_message.Message):
    __slots__ = ['amount', 'delegator_address', 'validator_address']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    delegator_address: str
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., amount: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=...) -> None:
        ...

class MsgUndelegateResponse(_message.Message):
    __slots__ = ['completion_time']
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    completion_time: _timestamp_pb2.Timestamp

    def __init__(self, completion_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...
