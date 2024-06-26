from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from ..models.webhook_get_dto_event_types_item import WebhookGetDtoEventTypesItem
import datetime
from typing import Union

if TYPE_CHECKING:
    from ..models.webhook_header_dto import WebhookHeaderDto


T = TypeVar("T", bound="WebhookGetDto")


@_attrs_define
class WebhookGetDto:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        ou_code (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        event_types (Union[Unset, List[WebhookGetDtoEventTypesItem]]):
        headers (Union[Unset, List['WebhookHeaderDto']]):
        url (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ou_code: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    event_types: Union[Unset, List[WebhookGetDtoEventTypesItem]] = UNSET
    headers: Union[Unset, List["WebhookHeaderDto"]] = UNSET
    url: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        ou_code = self.ou_code

        enabled = self.enabled

        event_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value
                event_types.append(event_types_item)

        headers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        url = self.url

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ou_code is not UNSET:
            field_dict["ouCode"] = ou_code
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if headers is not UNSET:
            field_dict["headers"] = headers
        if url is not UNSET:
            field_dict["url"] = url
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_header_dto import WebhookHeaderDto

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ou_code = d.pop("ouCode", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_types = []
        _event_types = d.pop("eventTypes", UNSET)
        for event_types_item_data in _event_types or []:
            event_types_item = WebhookGetDtoEventTypesItem(event_types_item_data)

            event_types.append(event_types_item)

        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = WebhookHeaderDto.from_dict(headers_item_data)

            headers.append(headers_item)

        url = d.pop("url", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset) or _created is None:
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset) or _updated is None:
            updated = UNSET
        else:
            updated = isoparse(_updated)

        webhook_get_dto = cls(
            id=id,
            name=name,
            ou_code=ou_code,
            enabled=enabled,
            event_types=event_types,
            headers=headers,
            url=url,
            created=created,
            updated=updated,
        )

        webhook_get_dto.additional_properties = d
        return webhook_get_dto

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
