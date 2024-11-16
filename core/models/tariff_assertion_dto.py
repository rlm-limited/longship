from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..models.tariff_assertion_dto_tariff_type import TariffAssertionDtoTariffType


T = TypeVar("T", bound="TariffAssertionDto")


@_attrs_define
class TariffAssertionDto:
    """
    Attributes:
        tariff_type (Union[Unset, TariffAssertionDtoTariffType]):  Default:
            TariffAssertionDtoTariffType.REIMBURSEMENTTARIFF.
        is_tariff_used (Union[Unset, bool]):
        tariff_result (Union[Unset, str]):
    """

    tariff_type: Union[Unset, TariffAssertionDtoTariffType] = (
        TariffAssertionDtoTariffType.REIMBURSEMENTTARIFF
    )
    is_tariff_used: Union[Unset, bool] = UNSET
    tariff_result: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff_type: Union[Unset, str] = UNSET
        if not isinstance(self.tariff_type, Unset):
            tariff_type = self.tariff_type.value

        is_tariff_used = self.is_tariff_used

        tariff_result = self.tariff_result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tariff_type is not UNSET:
            field_dict["tariffType"] = tariff_type
        if is_tariff_used is not UNSET:
            field_dict["isTariffUsed"] = is_tariff_used
        if tariff_result is not UNSET:
            field_dict["tariffResult"] = tariff_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tariff_type = d.pop("tariffType", UNSET)
        tariff_type: Union[Unset, TariffAssertionDtoTariffType]
        if isinstance(_tariff_type, Unset) or _tariff_type is None:
            tariff_type = UNSET
        else:
            tariff_type = TariffAssertionDtoTariffType(_tariff_type)

        is_tariff_used = d.pop("isTariffUsed", UNSET)

        tariff_result = d.pop("tariffResult", UNSET)

        tariff_assertion_dto = cls(
            tariff_type=tariff_type,
            is_tariff_used=is_tariff_used,
            tariff_result=tariff_result,
        )

        tariff_assertion_dto.additional_properties = d
        return tariff_assertion_dto

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
