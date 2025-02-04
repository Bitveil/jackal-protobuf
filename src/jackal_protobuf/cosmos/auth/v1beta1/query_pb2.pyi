
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryAccountRequest(_message.Message):
    __slots__ = ['address']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str

    def __init__(self, address: _Optional[str]=...) -> None:
        ...

class QueryAccountResponse(_message.Message):
    __slots__ = ['account']
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _any_pb2.Any

    def __init__(self, account: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=...) -> None:
        ...

class QueryAccountsRequest(_message.Message):
    __slots__ = ['pagination']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class QueryAccountsResponse(_message.Message):
    __slots__ = ['accounts', 'pagination']
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, accounts: _Optional[_Iterable[_Union[(_any_pb2.Any, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class QueryParamsRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class QueryParamsResponse(_message.Message):
    __slots__ = ['params']
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _auth_pb2.Params

    def __init__(self, params: _Optional[_Union[(_auth_pb2.Params, _Mapping)]]=...) -> None:
        ...
