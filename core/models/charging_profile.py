from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from ..models.charging_profile_charging_profile_kind import (
    ChargingProfileChargingProfileKind,
)
from ..models.charging_profile_charging_profile_purpose import (
    ChargingProfileChargingProfilePurpose,
)
import datetime
from typing import Union
from ..models.charging_profile_recurrency_kind import ChargingProfileRecurrencyKind

if TYPE_CHECKING:
    from ..models.charging_schedule import ChargingSchedule


T = TypeVar("T", bound="ChargingProfile")


@_attrs_define
class ChargingProfile:
    """
    Attributes:
        charging_profile_id (int):
        stack_level (int):
        charging_profile_purpose (ChargingProfileChargingProfilePurpose):  Default:
            ChargingProfileChargingProfilePurpose.CHARGEPOINTMAXPROFILE.
        charging_profile_kind (ChargingProfileChargingProfileKind):  Default:
            ChargingProfileChargingProfileKind.ABSOLUTE.
        charging_schedule (ChargingSchedule):
        transaction_id (Union[Unset, int]):
        recurrency_kind (Union[Unset, ChargingProfileRecurrencyKind]):  Default: ChargingProfileRecurrencyKind.DAILY.
        valid_from (Union[Unset, datetime.datetime]):
        valid_to (Union[Unset, datetime.datetime]):
    """

    charging_profile_id: int
    stack_level: int
    charging_schedule: "ChargingSchedule"
    charging_profile_purpose: ChargingProfileChargingProfilePurpose = (
        ChargingProfileChargingProfilePurpose.CHARGEPOINTMAXPROFILE
    )
    charging_profile_kind: ChargingProfileChargingProfileKind = (
        ChargingProfileChargingProfileKind.ABSOLUTE
    )
    transaction_id: Union[Unset, int] = UNSET
    recurrency_kind: Union[Unset, ChargingProfileRecurrencyKind] = (
        ChargingProfileRecurrencyKind.DAILY
    )
    valid_from: Union[Unset, datetime.datetime] = UNSET
    valid_to: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charging_profile_id = self.charging_profile_id

        stack_level = self.stack_level

        charging_profile_purpose = self.charging_profile_purpose.value

        charging_profile_kind = self.charging_profile_kind.value

        charging_schedule = self.charging_schedule.to_dict()

        transaction_id = self.transaction_id

        recurrency_kind: Union[Unset, str] = UNSET
        if not isinstance(self.recurrency_kind, Unset):
            recurrency_kind = self.recurrency_kind.value

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargingProfileId": charging_profile_id,
                "stackLevel": stack_level,
                "chargingProfilePurpose": charging_profile_purpose,
                "chargingProfileKind": charging_profile_kind,
                "chargingSchedule": charging_schedule,
            }
        )
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if recurrency_kind is not UNSET:
            field_dict["recurrencyKind"] = recurrency_kind
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charging_schedule import ChargingSchedule

        d = src_dict.copy()
        charging_profile_id = d.pop("chargingProfileId")

        stack_level = d.pop("stackLevel")

        charging_profile_purpose = ChargingProfileChargingProfilePurpose(
            d.pop("chargingProfilePurpose")
        )

        charging_profile_kind = ChargingProfileChargingProfileKind(
            d.pop("chargingProfileKind")
        )

        charging_schedule = ChargingSchedule.from_dict(d.pop("chargingSchedule"))

        transaction_id = d.pop("transactionId", UNSET)

        _recurrency_kind = d.pop("recurrencyKind", UNSET)
        recurrency_kind: Union[Unset, ChargingProfileRecurrencyKind]
        if isinstance(_recurrency_kind, Unset) or _recurrency_kind is None:
            recurrency_kind = UNSET
        else:
            recurrency_kind = ChargingProfileRecurrencyKind(_recurrency_kind)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset) or _valid_from is None:
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _valid_to = d.pop("validTo", UNSET)
        valid_to: Union[Unset, datetime.datetime]
        if isinstance(_valid_to, Unset) or _valid_to is None:
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to)

        charging_profile = cls(
            charging_profile_id=charging_profile_id,
            stack_level=stack_level,
            charging_profile_purpose=charging_profile_purpose,
            charging_profile_kind=charging_profile_kind,
            charging_schedule=charging_schedule,
            transaction_id=transaction_id,
            recurrency_kind=recurrency_kind,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        charging_profile.additional_properties = d
        return charging_profile

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
