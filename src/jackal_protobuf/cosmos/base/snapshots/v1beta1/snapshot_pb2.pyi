
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Metadata(_message.Message):
    __slots__ = ['chunk_hashes']
    CHUNK_HASHES_FIELD_NUMBER: _ClassVar[int]
    chunk_hashes: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, chunk_hashes: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class Snapshot(_message.Message):
    __slots__ = ['chunks', 'format', 'hash', 'height', 'metadata']
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    chunks: int
    format: int
    hash: bytes
    height: int
    metadata: Metadata

    def __init__(self, height: _Optional[int]=..., format: _Optional[int]=..., chunks: _Optional[int]=..., hash: _Optional[bytes]=..., metadata: _Optional[_Union[(Metadata, _Mapping)]]=...) -> None:
        ...

class SnapshotExtensionMeta(_message.Message):
    __slots__ = ['format', 'name']
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    format: int
    name: str

    def __init__(self, name: _Optional[str]=..., format: _Optional[int]=...) -> None:
        ...

class SnapshotExtensionPayload(_message.Message):
    __slots__ = ['payload']
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: bytes

    def __init__(self, payload: _Optional[bytes]=...) -> None:
        ...

class SnapshotIAVLItem(_message.Message):
    __slots__ = ['height', 'key', 'value', 'version']
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    height: int
    key: bytes
    value: bytes
    version: int

    def __init__(self, key: _Optional[bytes]=..., value: _Optional[bytes]=..., version: _Optional[int]=..., height: _Optional[int]=...) -> None:
        ...

class SnapshotItem(_message.Message):
    __slots__ = ['extension', 'extension_payload', 'iavl', 'store']
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IAVL_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    extension: SnapshotExtensionMeta
    extension_payload: SnapshotExtensionPayload
    iavl: SnapshotIAVLItem
    store: SnapshotStoreItem

    def __init__(self, store: _Optional[_Union[(SnapshotStoreItem, _Mapping)]]=..., iavl: _Optional[_Union[(SnapshotIAVLItem, _Mapping)]]=..., extension: _Optional[_Union[(SnapshotExtensionMeta, _Mapping)]]=..., extension_payload: _Optional[_Union[(SnapshotExtensionPayload, _Mapping)]]=...) -> None:
        ...

class SnapshotStoreItem(_message.Message):
    __slots__ = ['name']
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...
