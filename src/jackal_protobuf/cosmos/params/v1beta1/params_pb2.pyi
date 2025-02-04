
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParamChange(_message.Message):
    __slots__ = ['key', 'subspace', 'value']
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSPACE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    subspace: str
    value: str

    def __init__(self, subspace: _Optional[str]=..., key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class ParameterChangeProposal(_message.Message):
    __slots__ = ['changes', 'description', 'title']
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ParamChange]
    description: str
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., changes: _Optional[_Iterable[_Union[(ParamChange, _Mapping)]]]=...) -> None:
        ...
