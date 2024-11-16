from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.cs_charging_profiles import CsChargingProfiles


T = TypeVar("T", bound="SetChargingProfileRequest")


@_attrs_define
class SetChargingProfileRequest:
    """
    Attributes:
        connector_id (int):
        cs_charging_profiles (CsChargingProfiles):
    """

    connector_id: int
    cs_charging_profiles: "CsChargingProfiles"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        cs_charging_profiles = self.cs_charging_profiles.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "csChargingProfiles": cs_charging_profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cs_charging_profiles import CsChargingProfiles

        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        cs_charging_profiles = CsChargingProfiles.from_dict(d.pop("csChargingProfiles"))

        set_charging_profile_request = cls(
            connector_id=connector_id,
            cs_charging_profiles=cs_charging_profiles,
        )

        set_charging_profile_request.additional_properties = d
        return set_charging_profile_request

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
