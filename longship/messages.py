from core.models.message_log_dto import MessageLogDto
from core.api.chargepoints import get_all_chargepointmessages
from longship.client import LongshipClient
from typing import List
import json
from urllib.parse import urlparse, parse_qs


def get_messages(client: LongshipClient, chargepoint_id: str, message_id: str) -> List[MessageLogDto]:
    return get_all_chargepointmessages.sync_detailed(id=chargepoint_id, message_id=message_id, client=client.client, response_only=True)


def get_command_status(client: LongshipClient, chargepoint_id: str, location_url: str) -> str:
    message_id = parse_qs(urlparse(location_url).query)['messageId'][0]
    status = get_messages(chargepoint_id=chargepoint_id, message_id=message_id, client=client)
    return json.loads(status.parsed[0].payload)[2]['status']
