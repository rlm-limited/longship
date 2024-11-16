from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_local_list_request_update_type import SendLocalListRequestUpdateType
from typing import Union

if TYPE_CHECKING:
    from ..models.authorization_data import AuthorizationData


T = TypeVar("T", bound="SendLocalListRequest")


@_attrs_define
class SendLocalListRequest:
    """
    Attributes:
        list_version (int):
        update_type (SendLocalListRequestUpdateType):  Default: SendLocalListRequestUpdateType.DIFFERENTIAL.
        local_authorization_list (Union[Unset, List['AuthorizationData']]):
    """

    list_version: int
    update_type: SendLocalListRequestUpdateType = (
        SendLocalListRequestUpdateType.DIFFERENTIAL
    )
    local_authorization_list: Union[Unset, List["AuthorizationData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        list_version = self.list_version

        update_type = self.update_type.value

        local_authorization_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.local_authorization_list, Unset):
            local_authorization_list = []
            for local_authorization_list_item_data in self.local_authorization_list:
                local_authorization_list_item = (
                    local_authorization_list_item_data.to_dict()
                )
                local_authorization_list.append(local_authorization_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listVersion": list_version,
                "updateType": update_type,
            }
        )
        if local_authorization_list is not UNSET:
            field_dict["localAuthorizationList"] = local_authorization_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorization_data import AuthorizationData

        d = src_dict.copy()
        list_version = d.pop("listVersion")

        update_type = SendLocalListRequestUpdateType(d.pop("updateType"))

        local_authorization_list = []
        _local_authorization_list = d.pop("localAuthorizationList", UNSET)
        for local_authorization_list_item_data in _local_authorization_list or []:
            local_authorization_list_item = AuthorizationData.from_dict(
                local_authorization_list_item_data
            )

            local_authorization_list.append(local_authorization_list_item)

        send_local_list_request = cls(
            list_version=list_version,
            update_type=update_type,
            local_authorization_list=local_authorization_list,
        )

        send_local_list_request.additional_properties = d
        return send_local_list_request

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
