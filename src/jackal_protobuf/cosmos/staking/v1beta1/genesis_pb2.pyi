
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.staking.v1beta1 import staking_pb2 as _staking_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['delegations', 'exported', 'last_total_power', 'last_validator_powers', 'params', 'redelegations', 'unbonding_delegations', 'validators']
    DELEGATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_FIELD_NUMBER: _ClassVar[int]
    LAST_TOTAL_POWER_FIELD_NUMBER: _ClassVar[int]
    LAST_VALIDATOR_POWERS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    REDELEGATIONS_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_DELEGATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    delegations: _containers.RepeatedCompositeFieldContainer[_staking_pb2.Delegation]
    exported: bool
    last_total_power: bytes
    last_validator_powers: _containers.RepeatedCompositeFieldContainer[LastValidatorPower]
    params: _staking_pb2.Params
    redelegations: _containers.RepeatedCompositeFieldContainer[_staking_pb2.Redelegation]
    unbonding_delegations: _containers.RepeatedCompositeFieldContainer[_staking_pb2.UnbondingDelegation]
    validators: _containers.RepeatedCompositeFieldContainer[_staking_pb2.Validator]

    def __init__(self, params: _Optional[_Union[(_staking_pb2.Params, _Mapping)]]=..., last_total_power: _Optional[bytes]=..., last_validator_powers: _Optional[_Iterable[_Union[(LastValidatorPower, _Mapping)]]]=..., validators: _Optional[_Iterable[_Union[(_staking_pb2.Validator, _Mapping)]]]=..., delegations: _Optional[_Iterable[_Union[(_staking_pb2.Delegation, _Mapping)]]]=..., unbonding_delegations: _Optional[_Iterable[_Union[(_staking_pb2.UnbondingDelegation, _Mapping)]]]=..., redelegations: _Optional[_Iterable[_Union[(_staking_pb2.Redelegation, _Mapping)]]]=..., exported: bool=...) -> None:
        ...

class LastValidatorPower(_message.Message):
    __slots__ = ['address', 'power']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    address: str
    power: int

    def __init__(self, address: _Optional[str]=..., power: _Optional[int]=...) -> None:
        ...
