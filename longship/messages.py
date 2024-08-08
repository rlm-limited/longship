from longship_api_client.models.message_log_dto import MessageLogDto
from longship_api_client.api.chargepoints import get_all_chargepointmessages
from longship.client import LongshipClient
from typing import List
import json
import re


async def get_messages(client: LongshipClient, chargepoint_id: str, message_id: str) -> List[MessageLogDto]:
    return await get_all_chargepointmessages.asyncio_detailed(id=chargepoint_id, message_id=message_id, client=client.client, response_only=True)


async def get_command_status(client: LongshipClient, chargepoint_id: str, location_url: str) -> str:
    message_id = re.search(r'messageId=([a-f0-9]+)', location_url).group(1)
    status = get_messages(chargepoint_id=chargepoint_id, response_only=True, message_id=message_id, client=client.client)
    return json.loads(status.parsed[0].payload)[2]['status']
