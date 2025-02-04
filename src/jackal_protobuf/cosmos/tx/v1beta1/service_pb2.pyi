
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.abci.v1beta1 import abci_pb2 as _abci_pb2
from cosmos.tx.v1beta1 import tx_pb2 as _tx_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from tendermint.types import block_pb2 as _block_pb2
from tendermint.types import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
BROADCAST_MODE_ASYNC: BroadcastMode
BROADCAST_MODE_BLOCK: BroadcastMode
BROADCAST_MODE_SYNC: BroadcastMode
BROADCAST_MODE_UNSPECIFIED: BroadcastMode
DESCRIPTOR: _descriptor.FileDescriptor
ORDER_BY_ASC: OrderBy
ORDER_BY_DESC: OrderBy
ORDER_BY_UNSPECIFIED: OrderBy

class BroadcastTxRequest(_message.Message):
    __slots__ = ['mode', 'tx_bytes']
    MODE_FIELD_NUMBER: _ClassVar[int]
    TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    mode: BroadcastMode
    tx_bytes: bytes

    def __init__(self, tx_bytes: _Optional[bytes]=..., mode: _Optional[_Union[(BroadcastMode, str)]]=...) -> None:
        ...

class BroadcastTxResponse(_message.Message):
    __slots__ = ['tx_response']
    TX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    tx_response: _abci_pb2.TxResponse

    def __init__(self, tx_response: _Optional[_Union[(_abci_pb2.TxResponse, _Mapping)]]=...) -> None:
        ...

class GetBlockWithTxsRequest(_message.Message):
    __slots__ = ['height', 'pagination']
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    height: int
    pagination: _pagination_pb2.PageRequest

    def __init__(self, height: _Optional[int]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=...) -> None:
        ...

class GetBlockWithTxsResponse(_message.Message):
    __slots__ = ['block', 'block_id', 'pagination', 'txs']
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    TXS_FIELD_NUMBER: _ClassVar[int]
    block: _block_pb2.Block
    block_id: _types_pb2.BlockID
    pagination: _pagination_pb2.PageResponse
    txs: _containers.RepeatedCompositeFieldContainer[_tx_pb2.Tx]

    def __init__(self, txs: _Optional[_Iterable[_Union[(_tx_pb2.Tx, _Mapping)]]]=..., block_id: _Optional[_Union[(_types_pb2.BlockID, _Mapping)]]=..., block: _Optional[_Union[(_block_pb2.Block, _Mapping)]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class GetTxRequest(_message.Message):
    __slots__ = ['hash']
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str

    def __init__(self, hash: _Optional[str]=...) -> None:
        ...

class GetTxResponse(_message.Message):
    __slots__ = ['tx', 'tx_response']
    TX_FIELD_NUMBER: _ClassVar[int]
    TX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Tx
    tx_response: _abci_pb2.TxResponse

    def __init__(self, tx: _Optional[_Union[(_tx_pb2.Tx, _Mapping)]]=..., tx_response: _Optional[_Union[(_abci_pb2.TxResponse, _Mapping)]]=...) -> None:
        ...

class GetTxsEventRequest(_message.Message):
    __slots__ = ['events', 'order_by', 'pagination']
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[str]
    order_by: OrderBy
    pagination: _pagination_pb2.PageRequest

    def __init__(self, events: _Optional[_Iterable[str]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageRequest, _Mapping)]]=..., order_by: _Optional[_Union[(OrderBy, str)]]=...) -> None:
        ...

class GetTxsEventResponse(_message.Message):
    __slots__ = ['pagination', 'tx_responses', 'txs']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    TXS_FIELD_NUMBER: _ClassVar[int]
    TX_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageResponse
    tx_responses: _containers.RepeatedCompositeFieldContainer[_abci_pb2.TxResponse]
    txs: _containers.RepeatedCompositeFieldContainer[_tx_pb2.Tx]

    def __init__(self, txs: _Optional[_Iterable[_Union[(_tx_pb2.Tx, _Mapping)]]]=..., tx_responses: _Optional[_Iterable[_Union[(_abci_pb2.TxResponse, _Mapping)]]]=..., pagination: _Optional[_Union[(_pagination_pb2.PageResponse, _Mapping)]]=...) -> None:
        ...

class SimulateRequest(_message.Message):
    __slots__ = ['tx', 'tx_bytes']
    TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Tx
    tx_bytes: bytes

    def __init__(self, tx: _Optional[_Union[(_tx_pb2.Tx, _Mapping)]]=..., tx_bytes: _Optional[bytes]=...) -> None:
        ...

class SimulateResponse(_message.Message):
    __slots__ = ['gas_info', 'result']
    GAS_INFO_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    gas_info: _abci_pb2.GasInfo
    result: _abci_pb2.Result

    def __init__(self, gas_info: _Optional[_Union[(_abci_pb2.GasInfo, _Mapping)]]=..., result: _Optional[_Union[(_abci_pb2.Result, _Mapping)]]=...) -> None:
        ...

class OrderBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BroadcastMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
