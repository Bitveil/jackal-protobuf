
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from tendermint.p2p import types_pb2 as _types_pb2
from tendermint.types import block_pb2 as _block_pb2
from tendermint.types import types_pb2 as _types_pb2_1
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetBlockByHeightRequest(_message.Message):
    __slots__ = ['height']
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int

    def __init__(self, height: _Optional[int]=...) -> None:
        ...

class GetBlockByHeightResponse(_message.Message):
    __slots__ = ['block', 'block_id']
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    block: _block_pb2.Block
    block_id: _types_pb2_1.BlockID

    def __init__(self, block_id: _Optional[_Union[(_types_pb2_1.BlockID, _Mapping)]]=..., block: _Optional[_Union[(_block_pb2.Block, _Mapping)]]=...) -> None:
        ...

class GetLatestBlockRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class GetLatestBlockResponse(_message.Message):
    __slots__ = ['block', 'block_id']
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    block: _block_pb2.Block
    block_id: _types_pb2_1.BlockID

    def __init__(self, block_id: _Optional[_Union[(_types_pb2_1.BlockID, _Mapping)]]=..., block: _Optional[_Union[(_block_pb2.Block, _Mapping)]]=...) -> None:
        ...

class GetLatestValidatorSetRequest(_message.Message):
    __slots__ = ['pagination']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class GetLatestValidatorSetResponse(_message.Message):
    __slots__ = ['block_height', 'pagination', 'validators']
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    pagination: _pagination_pb2.PageResponse
    validators: _containers.RepeatedCompositeFieldContainer[Validator]

    def __init__(self, block_height: _Optional[int]=..., validators: _Optional[_Iterable[_Union[(Validator, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class GetNodeInfoRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class GetNodeInfoResponse(_message.Message):
    __slots__ = ['application_version', 'default_node_info']
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    application_version: VersionInfo
    default_node_info: _types_pb2.DefaultNodeInfo

    def __init__(self, default_node_info: _Optional[_Union[(_types_pb2.DefaultNodeInfo, _Mapping)]]=..., application_version: _Optional[_Union[(VersionInfo, _Mapping)]]=...) -> None:
        ...

class GetSyncingRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class GetSyncingResponse(_message.Message):
    __slots__ = ['syncing']
    SYNCING_FIELD_NUMBER: _ClassVar[int]
    syncing: bool

    def __init__(self, syncing: bool=...) -> None:
        ...

class GetValidatorSetByHeightRequest(_message.Message):
    __slots__ = ['height', 'pagination']
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    height: int
    pagination: _pagination_pb2.PageRequest

    def __init__(self, height: _Optional[int]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class GetValidatorSetByHeightResponse(_message.Message):
    __slots__ = ['block_height', 'pagination', 'validators']
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    pagination: _pagination_pb2.PageResponse
    validators: _containers.RepeatedCompositeFieldContainer[Validator]

    def __init__(self, block_height: _Optional[int]=..., validators: _Optional[_Iterable[_Union[(Validator, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class Module(_message.Message):
    __slots__ = ['path', 'sum', 'version']
    PATH_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    path: str
    sum: str
    version: str

    def __init__(self, path: _Optional[str]=..., version: _Optional[str]=..., sum: _Optional[str]=...) -> None:
        ...

class Validator(_message.Message):
    __slots__ = ['address', 'proposer_priority', 'pub_key', 'voting_power']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    VOTING_POWER_FIELD_NUMBER: _ClassVar[int]
    address: str
    proposer_priority: int
    pub_key: _any_pb2.Any
    voting_power: int

    def __init__(self, address: _Optional[str]=..., pub_key: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., voting_power: _Optional[int]=..., proposer_priority: _Optional[int]=...) -> None:
        ...

class VersionInfo(_message.Message):
    __slots__ = ['app_name', 'build_deps', 'build_tags', 'cosmos_sdk_version', 'git_commit', 'go_version', 'name', 'version']
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    BUILD_DEPS_FIELD_NUMBER: _ClassVar[int]
    BUILD_TAGS_FIELD_NUMBER: _ClassVar[int]
    COSMOS_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    GO_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    app_name: str
    build_deps: _containers.RepeatedCompositeFieldContainer[Module]
    build_tags: str
    cosmos_sdk_version: str
    git_commit: str
    go_version: str
    name: str
    version: str

    def __init__(self, name: _Optional[str]=..., app_name: _Optional[str]=..., version: _Optional[str]=..., git_commit: _Optional[str]=..., build_tags: _Optional[str]=..., go_version: _Optional[str]=..., build_deps: _Optional[_Iterable[_Union[(Module, _Mapping)]]]=..., cosmos_sdk_version: _Optional[str]=...) -> None:
        ...
