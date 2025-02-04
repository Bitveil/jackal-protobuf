
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenericAuthorization(_message.Message):
    __slots__ = ['msg']
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str

    def __init__(self, msg: _Optional[str]=...) -> None:
        ...

class Grant(_message.Message):
    __slots__ = ['authorization', 'expiration']
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    authorization: _any_pb2.Any
    expiration: _timestamp_pb2.Timestamp

    def __init__(self, authorization: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., expiration: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...

class GrantAuthorization(_message.Message):
    __slots__ = ['authorization', 'expiration', 'grantee', 'granter']
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    authorization: _any_pb2.Any
    expiration: _timestamp_pb2.Timestamp
    grantee: str
    granter: str

    def __init__(self, granter: _Optional[str]=..., grantee: _Optional[str]=..., authorization: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., expiration: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...
