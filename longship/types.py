from enum import Enum
from typing import Optional, Union

import attr

from core.models.chargepoint_dto_connectivity_status import (
    ChargepointDtoConnectivityStatus,
)
from core.models.connector_operational_status_dto_operational_status import (
    ConnectorOperationalStatusDtoOperationalStatus,
)


class WebhookPayloadType(str, Enum):
    ChargePointBooted = "ChargePointBooted"
    OperationalStatusChanged = "OperationalStatusChanged"
    ConnectivityStatusChanged = "ConnectivityStatusChanged"
    SessionStart = "SessionStart"
    SessionUpdate = "SessionUpdate"
    SessionStop = "SessionStop"
    CDRCreated = "CdrCreated"
    LocationCreated = "LocationCreated"
    LocationUpdated = "LocationUpdated"
    MSPInvoiceProposalStatus = "MspInvoiceProposalStatus"
    Ping = "Ping"

    def __str__(self) -> str:
        return str(self.value)


class RegistrationStatusType(str, Enum):
    Accepted = "Accepted"
    Pending = "Pending"

    def __str__(self) -> str:
        return str(self.value)


@attr.s(auto_attribs=True)
class ChargePointBootedData:
    registrationstatus: RegistrationStatusType


@attr.s(auto_attribs=True)
class OperationalStatusChangedData:
    status: ConnectorOperationalStatusDtoOperationalStatus
    errorcode: str
    connectornumber: int
    statussource: str
    locationid: Optional[str] = attr.ib(default=None)
    evseid: Optional[str] = attr.ib(default=None)
    vendorid: Optional[str] = attr.ib(default=None)
    vendorerrorcode: Optional[str] = attr.ib(default=None)


@attr.s(auto_attribs=True)
class ConnectivityStatusChangedData:
    # TODO: Longship uses uppercase for the status, but the webhook response uses CamelCase
    status: ChargepointDtoConnectivityStatus


@attr.s(auto_attribs=True)
class BaseSessionData:
    chargepointid: str
    connectornumber: int
    transactionid: str

@attr.s(auto_attribs=True)
class SessionStartData(BaseSessionData):
    locationid: Optional[str] = attr.ib(default=None)
    evseid: Optional[str] = attr.ib(default=None)


@attr.s(auto_attribs=True)
class SessionUpdateData(BaseSessionData):
    totalenergyinkwh: float
    totalduration: str
    totalcosts: float
    locationid: Optional[str] = attr.ib(default=None)
    evseid: Optional[str] = attr.ib(default=None)


@attr.s(auto_attribs=True)
class SessionStopData(SessionUpdateData):
    locationid: Optional[str] = attr.ib(default=None)
    evseid: Optional[str] = attr.ib(default=None)


@attr.s(auto_attribs=True)
class CDRCreatedData:
    chargepointid: str
    connectornumber: int
    totalenergyinkwh: float
    totalduration: str
    totalcosts: float
    transactionid: str
    locationid: Optional[str] = attr.ib(default=None)
    evseid: Optional[str] = attr.ib(default=None)


@attr.s(auto_attribs=True)
class LocationCreatedData:
    pass


@attr.s(auto_attribs=True)
class LocationUpdatedData:
    pass


@attr.s(auto_attribs=True)
class MSPInvoiceProposalStatusData:
    pass


@attr.s(auto_attribs=True)
class PingData:
    pass


@attr.s(auto_attribs=True)
class WebhookPayload:
    specversion: str
    id: str
    type: WebhookPayloadType
    subject: str
    time: str
    source: str
    datacontenttype: str
    data: Union[
        ChargePointBootedData,
        OperationalStatusChangedData,
        ConnectivityStatusChangedData,
        SessionStartData,
        SessionUpdateData,
        SessionStopData,
        CDRCreatedData,
        LocationCreatedData,
        LocationUpdatedData,
        MSPInvoiceProposalStatusData,
        PingData,
    ]

    def __attrs_post_init__(self):
        if self.type == WebhookPayloadType.ChargePointBooted:
            self.data = ChargePointBootedData(**self.data)
        elif self.type == WebhookPayloadType.OperationalStatusChanged:
            self.data = OperationalStatusChangedData(**self.data)
        elif self.type == WebhookPayloadType.ConnectivityStatusChanged:
            self.data["status"] = self.data["status"].upper()
            self.data = ConnectivityStatusChangedData(**self.data)
        elif self.type == WebhookPayloadType.SessionStart:
            self.data = SessionStartData(**self.data)
        elif self.type == WebhookPayloadType.SessionUpdate:
            self.data = SessionUpdateData(**self.data)
        elif self.type == WebhookPayloadType.SessionStop:
            self.data = SessionStopData(**self.data)
        elif self.type == WebhookPayloadType.CDRCreated:
            self.data = CDRCreatedData(**self.data)
        elif self.type == WebhookPayloadType.LocationCreated:
            self.data = LocationCreatedData(**self.data)
        elif self.type == WebhookPayloadType.LocationUpdated:
            self.data = LocationUpdatedData(**self.data)
        elif self.type == WebhookPayloadType.MSPInvoiceProposalStatus:
            self.data = MSPInvoiceProposalStatusData(**self.data)
        elif self.type == WebhookPayloadType.Ping:
            self.data = PingData(**self.data)
