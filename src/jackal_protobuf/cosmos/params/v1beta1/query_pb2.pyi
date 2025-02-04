
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.params.v1beta1 import params_pb2 as _params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ['key', 'subspace']
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSPACE_FIELD_NUMBER: _ClassVar[int]
    key: str
    subspace: str

    def __init__(self, subspace: _Optional[str]=..., key: _Optional[str]=...) -> None:
        ...

class QueryParamsResponse(_message.Message):
    __slots__ = ['param']
    PARAM_FIELD_NUMBER: _ClassVar[int]
    param: _params_pb2.ParamChange

    def __init__(self, param: _Optional[_Union[(_params_pb2.ParamChange, _Mapping)]]=...) -> None:
        ...
