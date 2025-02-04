
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['downtime_jail_duration', 'min_signed_per_window', 'signed_blocks_window', 'slash_fraction_double_sign', 'slash_fraction_downtime']
    DOWNTIME_JAIL_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_SIGNED_PER_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BLOCKS_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_DOUBLE_SIGN_FIELD_NUMBER: _ClassVar[int]
    SLASH_FRACTION_DOWNTIME_FIELD_NUMBER: _ClassVar[int]
    downtime_jail_duration: _duration_pb2.Duration
    min_signed_per_window: bytes
    signed_blocks_window: int
    slash_fraction_double_sign: bytes
    slash_fraction_downtime: bytes

    def __init__(self, signed_blocks_window: _Optional[int]=..., min_signed_per_window: _Optional[bytes]=..., downtime_jail_duration: _Optional[_Union[(_duration_pb2.Duration, _Mapping)]]=..., slash_fraction_double_sign: _Optional[bytes]=..., slash_fraction_downtime: _Optional[bytes]=...) -> None:
        ...

class ValidatorSigningInfo(_message.Message):
    __slots__ = ['address', 'index_offset', 'jailed_until', 'missed_blocks_counter', 'start_height', 'tombstoned']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    JAILED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    MISSED_BLOCKS_COUNTER_FIELD_NUMBER: _ClassVar[int]
    START_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOMBSTONED_FIELD_NUMBER: _ClassVar[int]
    address: str
    index_offset: int
    jailed_until: _timestamp_pb2.Timestamp
    missed_blocks_counter: int
    start_height: int
    tombstoned: bool

    def __init__(self, address: _Optional[str]=..., start_height: _Optional[int]=..., index_offset: _Optional[int]=..., jailed_until: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., tombstoned: bool=..., missed_blocks_counter: _Optional[int]=...) -> None:
        ...
