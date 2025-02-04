
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
AUTHORIZATION_TYPE_DELEGATE: AuthorizationType
AUTHORIZATION_TYPE_REDELEGATE: AuthorizationType
AUTHORIZATION_TYPE_UNDELEGATE: AuthorizationType
AUTHORIZATION_TYPE_UNSPECIFIED: AuthorizationType
DESCRIPTOR: _descriptor.FileDescriptor

class StakeAuthorization(_message.Message):
    __slots__ = ['allow_list', 'authorization_type', 'deny_list', 'max_tokens']

    class Validators(_message.Message):
        __slots__ = ['address']
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, address: _Optional[_Iterable[str]]=...) -> None:
            ...
    ALLOW_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DENY_LIST_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    allow_list: StakeAuthorization.Validators
    authorization_type: AuthorizationType
    deny_list: StakeAuthorization.Validators
    max_tokens: _coin_pb2.Coin

    def __init__(self, max_tokens: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=..., allow_list: _Optional[_Union[(StakeAuthorization.Validators, _Mapping)]]=..., deny_list: _Optional[_Union[(StakeAuthorization.Validators, _Mapping)]]=..., authorization_type: _Optional[_Union[(AuthorizationType, str)]]=...) -> None:
        ...

class AuthorizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
