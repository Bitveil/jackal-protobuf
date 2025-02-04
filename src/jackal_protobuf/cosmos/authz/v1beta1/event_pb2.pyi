
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventGrant(_message.Message):
    __slots__ = ['grantee', 'granter', 'msg_type_url']
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    granter: str
    msg_type_url: str

    def __init__(self, msg_type_url: _Optional[str]=..., granter: _Optional[str]=..., grantee: _Optional[str]=...) -> None:
        ...

class EventRevoke(_message.Message):
    __slots__ = ['grantee', 'granter', 'msg_type_url']
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    grantee: str
    granter: str
    msg_type_url: str

    def __init__(self, msg_type_url: _Optional[str]=..., granter: _Optional[str]=..., grantee: _Optional[str]=...) -> None:
        ...
