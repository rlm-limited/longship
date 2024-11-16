from core.models.chargepoint_dto import ChargepointDto
from core.models.chargepoint_status_dto import ChargepointStatusDto
from core.api.chargepoints import chargepoint_get, get_all_chargepoints
from core.api.chargepoint_status import chargepoint_status_get
from longship.client import LongshipClient


def get_chargepoint(client: LongshipClient, chargepoint_id: str) -> ChargepointDto:
    response = chargepoint_get.sync_detailed(id=chargepoint_id, client=client.client)
    return response.parsed


def get_chargepoint_status(client: LongshipClient, chargepoint_id: str) -> ChargepointStatusDto:
    response = chargepoint_status_get.sync_detailed(id=chargepoint_id, client=client.client)
    return response.parsed
