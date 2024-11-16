from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
import datetime
from typing import Union

if TYPE_CHECKING:
    from ..models.reimbursement_cdr_location_dto import ReimbursementCdrLocationDto
    from ..models.reimbursement_customer_share_dto import ReimbursementCustomerShareDto
    from ..models.reimburse_started_by_info_dto import ReimburseStartedByInfoDto
    from ..models.price_info_dto import PriceInfoDto


T = TypeVar("T", bound="ReimbursementCdrDto")


@_attrs_define
class ReimbursementCdrDto:
    """
    Attributes:
        id (Union[Unset, str]):
        tenant_id (Union[Unset, str]):
        charge_point_id (Union[Unset, str]):
        connector_id (Union[Unset, int]):
        location_id (Union[Unset, str]):
        evse_id (Union[Unset, str]):
        location (Union[Unset, ReimbursementCdrLocationDto]):
        start_datetime (Union[Unset, datetime.datetime]):
        end_date_time (Union[Unset, datetime.datetime]):
        session_id (Union[Unset, str]):
        started_by_info (Union[Unset, ReimburseStartedByInfoDto]):
        meter_start_in_wh (Union[Unset, int]):
        meter_stop_in_wh (Union[Unset, int]):
        total_energy_in_kwh (Union[Unset, float]):
        total_time_in_hours (Union[Unset, float]):
        total_price (Union[Unset, float]):
        created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        ou (Union[Unset, str]):
        ou_id (Union[Unset, str]):
        ou_name (Union[Unset, str]):
        reimburse_tariff_id (Union[Unset, str]):
        reimburse_tariff_name (Union[Unset, str]):
        reimburse_tariff_price (Union[Unset, float]):
        reimburse_tariff_calculated (Union[Unset, bool]):
        reimburse_price_calculated_on (Union[Unset, datetime.datetime]):
        bank_account (Union[Unset, str]):
        bank_account_created_on (Union[Unset, datetime.datetime]):
        bank_account_valid_from (Union[Unset, datetime.datetime]):
        reimburse_tariff_original_price (Union[Unset, float]):
        has_guest_charging_reimbursement_fee (Union[Unset, bool]):
        reimburse_tenant_fee (Union[Unset, float]):
        tenant_fee_calculated (Union[Unset, bool]):
        tariff_distribution_id (Union[Unset, str]):
        price_info (Union[Unset, PriceInfoDto]):
        customer_share (Union[Unset, float]):
        energy_compensation (Union[Unset, float]):
        reimbursement_customer_share (Union[Unset, ReimbursementCustomerShareDto]):
        local_start_date_time (Union[Unset, datetime.datetime]):
        local_end_date_time (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    charge_point_id: Union[Unset, str] = UNSET
    connector_id: Union[Unset, int] = UNSET
    location_id: Union[Unset, str] = UNSET
    evse_id: Union[Unset, str] = UNSET
    location: Union[Unset, "ReimbursementCdrLocationDto"] = UNSET
    start_datetime: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    session_id: Union[Unset, str] = UNSET
    started_by_info: Union[Unset, "ReimburseStartedByInfoDto"] = UNSET
    meter_start_in_wh: Union[Unset, int] = UNSET
    meter_stop_in_wh: Union[Unset, int] = UNSET
    total_energy_in_kwh: Union[Unset, float] = UNSET
    total_time_in_hours: Union[Unset, float] = UNSET
    total_price: Union[Unset, float] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    ou: Union[Unset, str] = UNSET
    ou_id: Union[Unset, str] = UNSET
    ou_name: Union[Unset, str] = UNSET
    reimburse_tariff_id: Union[Unset, str] = UNSET
    reimburse_tariff_name: Union[Unset, str] = UNSET
    reimburse_tariff_price: Union[Unset, float] = UNSET
    reimburse_tariff_calculated: Union[Unset, bool] = UNSET
    reimburse_price_calculated_on: Union[Unset, datetime.datetime] = UNSET
    bank_account: Union[Unset, str] = UNSET
    bank_account_created_on: Union[Unset, datetime.datetime] = UNSET
    bank_account_valid_from: Union[Unset, datetime.datetime] = UNSET
    reimburse_tariff_original_price: Union[Unset, float] = UNSET
    has_guest_charging_reimbursement_fee: Union[Unset, bool] = UNSET
    reimburse_tenant_fee: Union[Unset, float] = UNSET
    tenant_fee_calculated: Union[Unset, bool] = UNSET
    tariff_distribution_id: Union[Unset, str] = UNSET
    price_info: Union[Unset, "PriceInfoDto"] = UNSET
    customer_share: Union[Unset, float] = UNSET
    energy_compensation: Union[Unset, float] = UNSET
    reimbursement_customer_share: Union[Unset, "ReimbursementCustomerShareDto"] = UNSET
    local_start_date_time: Union[Unset, datetime.datetime] = UNSET
    local_end_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        charge_point_id = self.charge_point_id

        connector_id = self.connector_id

        location_id = self.location_id

        evse_id = self.evse_id

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        start_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.start_datetime, Unset):
            start_datetime = self.start_datetime.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        session_id = self.session_id

        started_by_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.started_by_info, Unset):
            started_by_info = self.started_by_info.to_dict()

        meter_start_in_wh = self.meter_start_in_wh

        meter_stop_in_wh = self.meter_stop_in_wh

        total_energy_in_kwh = self.total_energy_in_kwh

        total_time_in_hours = self.total_time_in_hours

        total_price = self.total_price

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        ou = self.ou

        ou_id = self.ou_id

        ou_name = self.ou_name

        reimburse_tariff_id = self.reimburse_tariff_id

        reimburse_tariff_name = self.reimburse_tariff_name

        reimburse_tariff_price = self.reimburse_tariff_price

        reimburse_tariff_calculated = self.reimburse_tariff_calculated

        reimburse_price_calculated_on: Union[Unset, str] = UNSET
        if not isinstance(self.reimburse_price_calculated_on, Unset):
            reimburse_price_calculated_on = (
                self.reimburse_price_calculated_on.isoformat()
            )

        bank_account = self.bank_account

        bank_account_created_on: Union[Unset, str] = UNSET
        if not isinstance(self.bank_account_created_on, Unset):
            bank_account_created_on = self.bank_account_created_on.isoformat()

        bank_account_valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.bank_account_valid_from, Unset):
            bank_account_valid_from = self.bank_account_valid_from.isoformat()

        reimburse_tariff_original_price = self.reimburse_tariff_original_price

        has_guest_charging_reimbursement_fee = self.has_guest_charging_reimbursement_fee

        reimburse_tenant_fee = self.reimburse_tenant_fee

        tenant_fee_calculated = self.tenant_fee_calculated

        tariff_distribution_id = self.tariff_distribution_id

        price_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_info, Unset):
            price_info = self.price_info.to_dict()

        customer_share = self.customer_share

        energy_compensation = self.energy_compensation

        reimbursement_customer_share: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reimbursement_customer_share, Unset):
            reimbursement_customer_share = self.reimbursement_customer_share.to_dict()

        local_start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.local_start_date_time, Unset):
            local_start_date_time = self.local_start_date_time.isoformat()

        local_end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.local_end_date_time, Unset):
            local_end_date_time = self.local_end_date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if charge_point_id is not UNSET:
            field_dict["chargePointId"] = charge_point_id
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if evse_id is not UNSET:
            field_dict["evseId"] = evse_id
        if location is not UNSET:
            field_dict["location"] = location
        if start_datetime is not UNSET:
            field_dict["startDatetime"] = start_datetime
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if started_by_info is not UNSET:
            field_dict["startedByInfo"] = started_by_info
        if meter_start_in_wh is not UNSET:
            field_dict["meterStartInWh"] = meter_start_in_wh
        if meter_stop_in_wh is not UNSET:
            field_dict["meterStopInWh"] = meter_stop_in_wh
        if total_energy_in_kwh is not UNSET:
            field_dict["totalEnergyInKwh"] = total_energy_in_kwh
        if total_time_in_hours is not UNSET:
            field_dict["totalTimeInHours"] = total_time_in_hours
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if created is not UNSET:
            field_dict["created"] = created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if ou is not UNSET:
            field_dict["ou"] = ou
        if ou_id is not UNSET:
            field_dict["ouId"] = ou_id
        if ou_name is not UNSET:
            field_dict["ouName"] = ou_name
        if reimburse_tariff_id is not UNSET:
            field_dict["reimburseTariffId"] = reimburse_tariff_id
        if reimburse_tariff_name is not UNSET:
            field_dict["reimburseTariffName"] = reimburse_tariff_name
        if reimburse_tariff_price is not UNSET:
            field_dict["reimburseTariffPrice"] = reimburse_tariff_price
        if reimburse_tariff_calculated is not UNSET:
            field_dict["reimburseTariffCalculated"] = reimburse_tariff_calculated
        if reimburse_price_calculated_on is not UNSET:
            field_dict["reimbursePriceCalculatedOn"] = reimburse_price_calculated_on
        if bank_account is not UNSET:
            field_dict["bankAccount"] = bank_account
        if bank_account_created_on is not UNSET:
            field_dict["bankAccountCreatedOn"] = bank_account_created_on
        if bank_account_valid_from is not UNSET:
            field_dict["bankAccountValidFrom"] = bank_account_valid_from
        if reimburse_tariff_original_price is not UNSET:
            field_dict["reimburseTariffOriginalPrice"] = reimburse_tariff_original_price
        if has_guest_charging_reimbursement_fee is not UNSET:
            field_dict["hasGuestChargingReimbursementFee"] = (
                has_guest_charging_reimbursement_fee
            )
        if reimburse_tenant_fee is not UNSET:
            field_dict["reimburseTenantFee"] = reimburse_tenant_fee
        if tenant_fee_calculated is not UNSET:
            field_dict["tenantFeeCalculated"] = tenant_fee_calculated
        if tariff_distribution_id is not UNSET:
            field_dict["tariffDistributionId"] = tariff_distribution_id
        if price_info is not UNSET:
            field_dict["priceInfo"] = price_info
        if customer_share is not UNSET:
            field_dict["customerShare"] = customer_share
        if energy_compensation is not UNSET:
            field_dict["energyCompensation"] = energy_compensation
        if reimbursement_customer_share is not UNSET:
            field_dict["reimbursementCustomerShare"] = reimbursement_customer_share
        if local_start_date_time is not UNSET:
            field_dict["localStartDateTime"] = local_start_date_time
        if local_end_date_time is not UNSET:
            field_dict["localEndDateTime"] = local_end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reimbursement_cdr_location_dto import ReimbursementCdrLocationDto
        from ..models.reimbursement_customer_share_dto import (
            ReimbursementCustomerShareDto,
        )
        from ..models.reimburse_started_by_info_dto import ReimburseStartedByInfoDto
        from ..models.price_info_dto import PriceInfoDto

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        charge_point_id = d.pop("chargePointId", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        location_id = d.pop("locationId", UNSET)

        evse_id = d.pop("evseId", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, ReimbursementCdrLocationDto]
        if isinstance(_location, Unset) or _location is None:
            location = UNSET
        else:
            location = ReimbursementCdrLocationDto.from_dict(_location)

        _start_datetime = d.pop("startDatetime", UNSET)
        start_datetime: Union[Unset, datetime.datetime]
        if isinstance(_start_datetime, Unset) or _start_datetime is None:
            start_datetime = UNSET
        else:
            start_datetime = isoparse(_start_datetime)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time, Unset) or _end_date_time is None:
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        session_id = d.pop("sessionId", UNSET)

        _started_by_info = d.pop("startedByInfo", UNSET)
        started_by_info: Union[Unset, ReimburseStartedByInfoDto]
        if isinstance(_started_by_info, Unset) or _started_by_info is None:
            started_by_info = UNSET
        else:
            started_by_info = ReimburseStartedByInfoDto.from_dict(_started_by_info)

        meter_start_in_wh = d.pop("meterStartInWh", UNSET)

        meter_stop_in_wh = d.pop("meterStopInWh", UNSET)

        total_energy_in_kwh = d.pop("totalEnergyInKwh", UNSET)

        total_time_in_hours = d.pop("totalTimeInHours", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset) or _created is None:
            created = UNSET
        else:
            created = isoparse(_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset) or _last_updated is None:
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        ou = d.pop("ou", UNSET)

        ou_id = d.pop("ouId", UNSET)

        ou_name = d.pop("ouName", UNSET)

        reimburse_tariff_id = d.pop("reimburseTariffId", UNSET)

        reimburse_tariff_name = d.pop("reimburseTariffName", UNSET)

        reimburse_tariff_price = d.pop("reimburseTariffPrice", UNSET)

        reimburse_tariff_calculated = d.pop("reimburseTariffCalculated", UNSET)

        _reimburse_price_calculated_on = d.pop("reimbursePriceCalculatedOn", UNSET)
        reimburse_price_calculated_on: Union[Unset, datetime.datetime]
        if isinstance(_reimburse_price_calculated_on, Unset) or _reimburse_price_calculated_on is None:
            reimburse_price_calculated_on = UNSET
        else:
            reimburse_price_calculated_on = isoparse(_reimburse_price_calculated_on)

        bank_account = d.pop("bankAccount", UNSET)

        _bank_account_created_on = d.pop("bankAccountCreatedOn", UNSET)
        bank_account_created_on: Union[Unset, datetime.datetime]
        if isinstance(_bank_account_created_on, Unset) or _bank_account_created_on is None:
            bank_account_created_on = UNSET
        else:
            bank_account_created_on = isoparse(_bank_account_created_on)

        _bank_account_valid_from = d.pop("bankAccountValidFrom", UNSET)
        bank_account_valid_from: Union[Unset, datetime.datetime]
        if isinstance(_bank_account_valid_from, Unset) or _bank_account_valid_from is None:
            bank_account_valid_from = UNSET
        else:
            bank_account_valid_from = isoparse(_bank_account_valid_from)

        reimburse_tariff_original_price = d.pop("reimburseTariffOriginalPrice", UNSET)

        has_guest_charging_reimbursement_fee = d.pop(
            "hasGuestChargingReimbursementFee", UNSET
        )

        reimburse_tenant_fee = d.pop("reimburseTenantFee", UNSET)

        tenant_fee_calculated = d.pop("tenantFeeCalculated", UNSET)

        tariff_distribution_id = d.pop("tariffDistributionId", UNSET)

        _price_info = d.pop("priceInfo", UNSET)
        price_info: Union[Unset, PriceInfoDto]
        if isinstance(_price_info, Unset) or _price_info is None:
            price_info = UNSET
        else:
            price_info = PriceInfoDto.from_dict(_price_info)

        customer_share = d.pop("customerShare", UNSET)

        energy_compensation = d.pop("energyCompensation", UNSET)

        _reimbursement_customer_share = d.pop("reimbursementCustomerShare", UNSET)
        reimbursement_customer_share: Union[Unset, ReimbursementCustomerShareDto]
        if isinstance(_reimbursement_customer_share, Unset) or _reimbursement_customer_share is None:
            reimbursement_customer_share = UNSET
        else:
            reimbursement_customer_share = ReimbursementCustomerShareDto.from_dict(
                _reimbursement_customer_share
            )

        _local_start_date_time = d.pop("localStartDateTime", UNSET)
        local_start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_local_start_date_time, Unset) or _local_start_date_time is None:
            local_start_date_time = UNSET
        else:
            local_start_date_time = isoparse(_local_start_date_time)

        _local_end_date_time = d.pop("localEndDateTime", UNSET)
        local_end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_local_end_date_time, Unset) or _local_end_date_time is None:
            local_end_date_time = UNSET
        else:
            local_end_date_time = isoparse(_local_end_date_time)

        reimbursement_cdr_dto = cls(
            id=id,
            tenant_id=tenant_id,
            charge_point_id=charge_point_id,
            connector_id=connector_id,
            location_id=location_id,
            evse_id=evse_id,
            location=location,
            start_datetime=start_datetime,
            end_date_time=end_date_time,
            session_id=session_id,
            started_by_info=started_by_info,
            meter_start_in_wh=meter_start_in_wh,
            meter_stop_in_wh=meter_stop_in_wh,
            total_energy_in_kwh=total_energy_in_kwh,
            total_time_in_hours=total_time_in_hours,
            total_price=total_price,
            created=created,
            last_updated=last_updated,
            ou=ou,
            ou_id=ou_id,
            ou_name=ou_name,
            reimburse_tariff_id=reimburse_tariff_id,
            reimburse_tariff_name=reimburse_tariff_name,
            reimburse_tariff_price=reimburse_tariff_price,
            reimburse_tariff_calculated=reimburse_tariff_calculated,
            reimburse_price_calculated_on=reimburse_price_calculated_on,
            bank_account=bank_account,
            bank_account_created_on=bank_account_created_on,
            bank_account_valid_from=bank_account_valid_from,
            reimburse_tariff_original_price=reimburse_tariff_original_price,
            has_guest_charging_reimbursement_fee=has_guest_charging_reimbursement_fee,
            reimburse_tenant_fee=reimburse_tenant_fee,
            tenant_fee_calculated=tenant_fee_calculated,
            tariff_distribution_id=tariff_distribution_id,
            price_info=price_info,
            customer_share=customer_share,
            energy_compensation=energy_compensation,
            reimbursement_customer_share=reimbursement_customer_share,
            local_start_date_time=local_start_date_time,
            local_end_date_time=local_end_date_time,
        )

        reimbursement_cdr_dto.additional_properties = d
        return reimbursement_cdr_dto

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
