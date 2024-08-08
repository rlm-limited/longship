from longship_api_client.models.remote_start_transaction_request import RemoteStartTransactionRequest
from longship_api_client.models.remote_stop_transaction_request import RemoteStopTransactionRequest
from longship_api_client.models.session_dto import SessionDto
from longship_api_client.api.sessions import session_get, get_all_sessions
from longship_api_client.api.commands import send_remote_start_transaction_request, send_remote_stop_transaction_request
from longship.client import LongshipClient
import json


async def get_session_with_id(client: LongshipClient, session_id: str) -> SessionDto:
    session = await session_get.asyncio_detailed(id=session_id, client=client.client)
    return session.parsed


async def get_session_id(client: LongshipClient, chargepoint_id: str = None, connector_number: str = None, running_only: bool = True) -> list[SessionDto]:
    response = await get_all_sessions.asyncio_detailed(chargepoint_id=chargepoint_id, connector_number=connector_number, running_only=running_only, client=client.client)
    return response.parsed[0]


async def send_remote_start_session_command(client: LongshipClient, chargepoint_id: str, connector_id: int , id_tag: str) -> str:
    response = await send_remote_start_transaction_request.asyncio_detailed(id=chargepoint_id, client=client.client, body=RemoteStartTransactionRequest(id_tag=id_tag, connector_id=connector_id))
    if response.status_code != 202:
        raise ValueError(f"Failed to send remote start session command: {json.loads(response.content.decode('utf8'))['errorDetails']['message']}")
    return response.headers['location']


async def send_remote_stop_session_command(client: LongshipClient, chargepoint_id: str, session_id: str) -> str:
    session = await get_session_with_id(session_id=session_id)
    response = await send_remote_stop_transaction_request.asyncio_detailed(id=chargepoint_id, body=RemoteStopTransactionRequest(transaction_id=session['transaction_id']), client=client.client)
    if response.status_code != 202:
        raise ValueError(f"Failed to send remote stop session command: {json.loads(response.content.decode('utf8'))['errorDetails']['message']}")
    return response.headers['location']
