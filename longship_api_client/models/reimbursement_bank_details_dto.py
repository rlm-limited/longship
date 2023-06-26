import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReimbursementBankDetailsDto")


@attr.s(auto_attribs=True)
class ReimbursementBankDetailsDto:
    """
    Attributes:
        bankaccount (Union[Unset, str]):
        date_created (Union[Unset, datetime.datetime]):
        valid_from (Union[Unset, datetime.datetime]):
    """

    bankaccount: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bankaccount = self.bankaccount
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bankaccount is not UNSET:
            field_dict["bankaccount"] = bankaccount
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bankaccount = d.pop("bankaccount", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        reimbursement_bank_details_dto = cls(
            bankaccount=bankaccount,
            date_created=date_created,
            valid_from=valid_from,
        )

        reimbursement_bank_details_dto.additional_properties = d
        return reimbursement_bank_details_dto

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
