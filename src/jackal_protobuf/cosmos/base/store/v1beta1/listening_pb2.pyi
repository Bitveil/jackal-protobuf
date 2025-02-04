
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class StoreKVPair(_message.Message):
    __slots__ = ['delete', 'key', 'store_key', 'value']
    DELETE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STORE_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    delete: bool
    key: bytes
    store_key: str
    value: bytes

    def __init__(self, store_key: _Optional[str]=..., delete: bool=..., key: _Optional[bytes]=..., value: _Optional[bytes]=...) -> None:
        ...
