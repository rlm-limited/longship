from longship_api_client.models.chargepoint_dto import ChargepointDto
from longship_api_client.models.chargepoint_status_dto import ChargepointStatusDto
from longship_api_client.api.chargepoints import chargepoint_get
from longship_api_client.api.chargepoint_status import chargepoint_status_get
from longship.client import LongshipClient


async def get_chargepoint(client: LongshipClient, chargepoint_id: str) -> ChargepointDto:
    response = await chargepoint_get.asyncio_detailed(id=chargepoint_id, client=client.client)
    return response.parsed


async def get_chargepoint_status(client: LongshipClient, chargepoint_id: str) -> ChargepointStatusDto:
    response = await chargepoint_status_get.asyncio_detailed(id=chargepoint_id, client=client.client)
    return response.parsed
