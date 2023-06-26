from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.energy_source_dto_source import EnergySourceDtoSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergySourceDto")


@attr.s(auto_attribs=True)
class EnergySourceDto:
    """
    Attributes:
        source (Union[Unset, EnergySourceDtoSource]):  Default: EnergySourceDtoSource.NUCLEAR.
        percentage (Union[Unset, int]):
    """

    source: Union[Unset, EnergySourceDtoSource] = EnergySourceDtoSource.NUCLEAR
    percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        percentage = self.percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source = d.pop("source", UNSET)
        source: Union[Unset, EnergySourceDtoSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = EnergySourceDtoSource(_source)

        percentage = d.pop("percentage", UNSET)

        energy_source_dto = cls(
            source=source,
            percentage=percentage,
        )

        energy_source_dto.additional_properties = d
        return energy_source_dto

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
