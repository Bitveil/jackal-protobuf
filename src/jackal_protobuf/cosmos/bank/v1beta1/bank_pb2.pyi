
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DenomUnit(_message.Message):
    __slots__ = ['aliases', 'denom', 'exponent']
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    EXPONENT_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    denom: str
    exponent: int

    def __init__(self, denom: _Optional[str]=..., exponent: _Optional[int]=..., aliases: _Optional[_Iterable[str]]=...) -> None:
        ...

class Input(_message.Message):
    __slots__ = ['address', 'coins']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COINS_FIELD_NUMBER: _ClassVar[int]
    address: str
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, address: _Optional[str]=..., coins: _Optional[_Iterable[_Union[(_coin_pb2.Coin, _Mapping)]]]=...) -> None:
        ...

class Metadata(_message.Message):
    __slots__ = ['base', 'denom_units', 'description', 'display', 'name', 'symbol']
    BASE_FIELD_NUMBER: _ClassVar[int]
    DENOM_UNITS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    base: str
    denom_units: _containers.RepeatedCompositeFieldContainer[DenomUnit]
    description: str
    display: str
    name: str
    symbol: str

    def __init__(self, description: _Optional[str]=..., denom_units: _Optional[_Iterable[_Union[(DenomUnit, _Mapping)]]]=..., base: _Optional[str]=..., display: _Optional[str]=..., name: _Optional[str]=..., symbol: _Optional[str]=...) -> None:
        ...

class Output(_message.Message):
    __slots__ = ['address', 'coins']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COINS_FIELD_NUMBER: _ClassVar[int]
    address: str
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, address: _Optional[str]=..., coins: _Optional[_Iterable[_Union[(_coin_pb2.Coin, _Mapping)]]]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ['default_send_enabled', 'send_enabled']
    DEFAULT_SEND_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SEND_ENABLED_FIELD_NUMBER: _ClassVar[int]
    default_send_enabled: bool
    send_enabled: _containers.RepeatedCompositeFieldContainer[SendEnabled]

    def __init__(self, send_enabled: _Optional[_Iterable[_Union[(SendEnabled, _Mapping)]]]=..., default_send_enabled: bool=...) -> None:
        ...

class SendEnabled(_message.Message):
    __slots__ = ['denom', 'enabled']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    denom: str
    enabled: bool

    def __init__(self, denom: _Optional[str]=..., enabled: bool=...) -> None:
        ...

class Supply(_message.Message):
    __slots__ = ['total']
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    total: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, total: _Optional[_Iterable[_Union[(_coin_pb2.Coin, _Mapping)]]]=...) -> None:
        ...
