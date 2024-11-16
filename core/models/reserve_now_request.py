from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
import datetime
from typing import Union


T = TypeVar("T", bound="ReserveNowRequest")


@_attrs_define
class ReserveNowRequest:
    """
    Attributes:
        connector_id (int):
        expiry_date (datetime.datetime):
        id_tag (str):
        reservation_id (int):
        parent_id_tag (Union[Unset, str]):
    """

    connector_id: int
    expiry_date: datetime.datetime
    id_tag: str
    reservation_id: int
    parent_id_tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        expiry_date = self.expiry_date.isoformat()

        id_tag = self.id_tag

        reservation_id = self.reservation_id

        parent_id_tag = self.parent_id_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "expiryDate": expiry_date,
                "idTag": id_tag,
                "reservationId": reservation_id,
            }
        )
        if parent_id_tag is not UNSET:
            field_dict["parentIdTag"] = parent_id_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connector_id = d.pop("connectorId")

        expiry_date = isoparse(d.pop("expiryDate"))

        id_tag = d.pop("idTag")

        reservation_id = d.pop("reservationId")

        parent_id_tag = d.pop("parentIdTag", UNSET)

        reserve_now_request = cls(
            connector_id=connector_id,
            expiry_date=expiry_date,
            id_tag=id_tag,
            reservation_id=reservation_id,
            parent_id_tag=parent_id_tag,
        )

        reserve_now_request.additional_properties = d
        return reserve_now_request

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
