
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from tendermint.types import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
BOND_STATUS_BONDED: BondStatus
BOND_STATUS_UNBONDED: BondStatus
BOND_STATUS_UNBONDING: BondStatus
BOND_STATUS_UNSPECIFIED: BondStatus
DESCRIPTOR: _descriptor.FileDescriptor

class Commission(_message.Message):
    __slots__ = ['commission_rates', 'update_time']
    COMMISSION_RATES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    commission_rates: CommissionRates
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, commission_rates: _Optional[_Union[(CommissionRates, _Mapping)]]=..., update_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...

class CommissionRates(_message.Message):
    __slots__ = ['max_change_rate', 'max_rate', 'rate']
    MAX_CHANGE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    max_change_rate: str
    max_rate: str
    rate: str

    def __init__(self, rate: _Optional[str]=..., max_rate: _Optional[str]=..., max_change_rate: _Optional[str]=...) -> None:
        ...

class DVPair(_message.Message):
    __slots__ = ['delegator_address', 'validator_address']
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=...) -> None:
        ...

class DVPairs(_message.Message):
    __slots__ = ['pairs']
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    pairs: _containers.RepeatedCompositeFieldContainer[DVPair]

    def __init__(self, pairs: _Optional[_Iterable[_Union[(DVPair, _Mapping)]]]=...) -> None:
        ...

class DVVTriplet(_message.Message):
    __slots__ = ['delegator_address', 'validator_dst_address', 'validator_src_address']
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_DST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SRC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_dst_address: str
    validator_src_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_src_address: _Optional[str]=..., validator_dst_address: _Optional[str]=...) -> None:
        ...

class DVVTriplets(_message.Message):
    __slots__ = ['triplets']
    TRIPLETS_FIELD_NUMBER: _ClassVar[int]
    triplets: _containers.RepeatedCompositeFieldContainer[DVVTriplet]

    def __init__(self, triplets: _Optional[_Iterable[_Union[(DVVTriplet, _Mapping)]]]=...) -> None:
        ...

class Delegation(_message.Message):
    __slots__ = ['delegator_address', 'shares', 'validator_address']
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHARES_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    shares: str
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., shares: _Optional[str]=...) -> None:
        ...

class DelegationResponse(_message.Message):
    __slots__ = ['balance', 'delegation']
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DELEGATION_FIELD_NUMBER: _ClassVar[int]
    balance: _coin_pb2.Coin
    delegation: Delegation

    def __init__(self, delegation: _Optional[_Union[(Delegation, _Mapping)]]=..., balance: _Optional[_Union[(_coin_pb2.Coin, _Mapping)]]=...) -> None:
        ...

class Description(_message.Message):
    __slots__ = ['details', 'identity', 'moniker', 'security_contact', 'website']
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    details: str
    identity: str
    moniker: str
    security_contact: str
    website: str

    def __init__(self, moniker: _Optional[str]=..., identity: _Optional[str]=..., website: _Optional[str]=..., security_contact: _Optional[str]=..., details: _Optional[str]=...) -> None:
        ...

class HistoricalInfo(_message.Message):
    __slots__ = ['header', 'valset']
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VALSET_FIELD_NUMBER: _ClassVar[int]
    header: _types_pb2.Header
    valset: _containers.RepeatedCompositeFieldContainer[Validator]

    def __init__(self, header: _Optional[_Union[(_types_pb2.Header, _Mapping)]]=..., valset: _Optional[_Iterable[_Union[(Validator, _Mapping)]]]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ['bond_denom', 'historical_entries', 'max_entries', 'max_validators', 'unbonding_time']
    BOND_DENOM_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_TIME_FIELD_NUMBER: _ClassVar[int]
    bond_denom: str
    historical_entries: int
    max_entries: int
    max_validators: int
    unbonding_time: _duration_pb2.Duration

    def __init__(self, unbonding_time: _Optional[_Union[(_duration_pb2.Duration, _Mapping)]]=..., max_validators: _Optional[int]=..., max_entries: _Optional[int]=..., historical_entries: _Optional[int]=..., bond_denom: _Optional[str]=...) -> None:
        ...

class Pool(_message.Message):
    __slots__ = ['bonded_tokens', 'not_bonded_tokens']
    BONDED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    NOT_BONDED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    bonded_tokens: str
    not_bonded_tokens: str

    def __init__(self, not_bonded_tokens: _Optional[str]=..., bonded_tokens: _Optional[str]=...) -> None:
        ...

class Redelegation(_message.Message):
    __slots__ = ['delegator_address', 'entries', 'validator_dst_address', 'validator_src_address']
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_DST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SRC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    entries: _containers.RepeatedCompositeFieldContainer[RedelegationEntry]
    validator_dst_address: str
    validator_src_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_src_address: _Optional[str]=..., validator_dst_address: _Optional[str]=..., entries: _Optional[_Iterable[_Union[(RedelegationEntry, _Mapping)]]]=...) -> None:
        ...

class RedelegationEntry(_message.Message):
    __slots__ = ['completion_time', 'creation_height', 'initial_balance', 'shares_dst']
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SHARES_DST_FIELD_NUMBER: _ClassVar[int]
    completion_time: _timestamp_pb2.Timestamp
    creation_height: int
    initial_balance: str
    shares_dst: str

    def __init__(self, creation_height: _Optional[int]=..., completion_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., initial_balance: _Optional[str]=..., shares_dst: _Optional[str]=...) -> None:
        ...

class RedelegationEntryResponse(_message.Message):
    __slots__ = ['balance', 'redelegation_entry']
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    REDELEGATION_ENTRY_FIELD_NUMBER: _ClassVar[int]
    balance: str
    redelegation_entry: RedelegationEntry

    def __init__(self, redelegation_entry: _Optional[_Union[(RedelegationEntry, _Mapping)]]=..., balance: _Optional[str]=...) -> None:
        ...

class RedelegationResponse(_message.Message):
    __slots__ = ['entries', 'redelegation']
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REDELEGATION_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RedelegationEntryResponse]
    redelegation: Redelegation

    def __init__(self, redelegation: _Optional[_Union[(Redelegation, _Mapping)]]=..., entries: _Optional[_Iterable[_Union[(RedelegationEntryResponse, _Mapping)]]]=...) -> None:
        ...

class UnbondingDelegation(_message.Message):
    __slots__ = ['delegator_address', 'entries', 'validator_address']
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    entries: _containers.RepeatedCompositeFieldContainer[UnbondingDelegationEntry]
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., entries: _Optional[_Iterable[_Union[(UnbondingDelegationEntry, _Mapping)]]]=...) -> None:
        ...

class UnbondingDelegationEntry(_message.Message):
    __slots__ = ['balance', 'completion_time', 'creation_height', 'initial_balance']
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: str
    completion_time: _timestamp_pb2.Timestamp
    creation_height: int
    initial_balance: str

    def __init__(self, creation_height: _Optional[int]=..., completion_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., initial_balance: _Optional[str]=..., balance: _Optional[str]=...) -> None:
        ...

class ValAddresses(_message.Message):
    __slots__ = ['addresses']
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, addresses: _Optional[_Iterable[str]]=...) -> None:
        ...

class Validator(_message.Message):
    __slots__ = ['commission', 'consensus_pubkey', 'delegator_shares', 'description', 'jailed', 'min_self_delegation', 'operator_address', 'status', 'tokens', 'unbonding_height', 'unbonding_time']
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_SHARES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    JAILED_FIELD_NUMBER: _ClassVar[int]
    MIN_SELF_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_TIME_FIELD_NUMBER: _ClassVar[int]
    commission: Commission
    consensus_pubkey: _any_pb2.Any
    delegator_shares: str
    description: Description
    jailed: bool
    min_self_delegation: str
    operator_address: str
    status: BondStatus
    tokens: str
    unbonding_height: int
    unbonding_time: _timestamp_pb2.Timestamp

    def __init__(self, operator_address: _Optional[str]=..., consensus_pubkey: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., jailed: bool=..., status: _Optional[_Union[(BondStatus, str)]]=..., tokens: _Optional[str]=..., delegator_shares: _Optional[str]=..., description: _Optional[_Union[(Description, _Mapping)]]=..., unbonding_height: _Optional[int]=..., unbonding_time: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., commission: _Optional[_Union[(Commission, _Mapping)]]=..., min_self_delegation: _Optional[str]=...) -> None:
        ...

class BondStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
