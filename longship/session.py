from longship_api_client.models.remote_start_transaction_request import RemoteStartTransactionRequest
from longship_api_client.models.remote_stop_transaction_request import RemoteStopTransactionRequest
from longship_api_client.models.session_dto import SessionDto
from longship_api_client.api.sessions import session_get, get_all_sessions
from longship_api_client.api.commands import send_remote_start_transaction_request, send_remote_stop_transaction_request
from longship.client import LongshipClient
from longship.messages import get_command_status
import json
import time
from typing import List
import logging


logger = logging.getLogger(__name__)


def filter_sessions(client: LongshipClient, chargepoint_id=None, connector_id=None, running_only=True) -> List[SessionDto]:
    response = get_all_sessions.sync_detailed(chargepoint_id=chargepoint_id, connector_number=connector_id, running_only=running_only, client=client.client)
    return response


def get_session_status_with_id(client: LongshipClient, session_id: str) -> SessionDto:
    response = session_get.sync_detailed(id=session_id, client=client.client)
    return response.parsed


def get_session_id(client: LongshipClient, chargepoint_id: str = None, connector_number: str = None, running_only: bool = True) -> list[SessionDto]:
    response = get_all_sessions.sync_detailed(chargepoint_id=chargepoint_id, connector_number=connector_number, running_only=running_only, client=client.client)
    return response.parsed[0]


def remote_start_session(client: LongshipClient, chargepoint_id: str, connector_id: int , id_tag: str) -> str:
    try:
        response = send_remote_start_transaction_request.sync_detailed(id=chargepoint_id, client=client.client, body=RemoteStartTransactionRequest(id_tag=id_tag, connector_id=connector_id))
        if response.status_code != 202:
            logging.CRITICAL(f"Failed to send remote start session command: {json.loads(response.content.decode('utf8'))['errorDetails']['message']}")
        time.sleep(5)
        status = get_command_status(chargepoint_id=chargepoint_id, location_url=response.headers['location'], client=client)
        if status == 'Accepted':
            time.sleep(10)
            session = filter_sessions(client=client, chargepoint_id=chargepoint_id, connector_id=connector_id, running_only=True)
            logging.INFO(f"Remote Start Command at chargepoint: {chargepoint_id} with Id Tag: {id_tag} was {status}!")
            session_id = json.loads(session.content.decode("utf-8"))[0]['id']
            if len(session_id) == 0:
                logging.CRITICAL(f"Failed to retrieve session id with chargepoint: {chargepoint_id} and id tag: {id_tag}")
            return session_id
        else:
            logging.INFO(f"Remote Start Command at chargepoint: {chargepoint_id} with Id Tag: {id_tag} was {status}!")
    except IndexError as e:
        logging.error(f"Failed to retrieve session id with chargepoint: {chargepoint_id} and id tag: {id_tag}", exc_info=e)
    except Exception as e:
        logging.error(f"Failed to start session with chargepoint: {chargepoint_id} and id tag: {id_tag}", exc_info=e)


def remote_stop_session(client: LongshipClient, chargepoint_id: str, session_id: str) -> str:
    try:
        session = get_session_status_with_id(session_id=session_id, client=client)
        response = send_remote_stop_transaction_request.sync_detailed(id=chargepoint_id, body=RemoteStopTransactionRequest(transaction_id=session.transaction_id), client=client.client)
        if response.status_code != 202:
            logging.CRITICAL(f"Failed to send remote stop session command: {json.loads(response.content.decode('utf8'))['errorDetails']['message']}")
        time.sleep(5)
        status = get_command_status(chargepoint_id=chargepoint_id, location_url=response.headers['location'], client=client)
        if status == 'Accepted':
            return session_id
        else:
            logging.INFO(f"Remote Stop Command at chargepoint: {chargepoint_id} with Session Id: {session_id} was {status}!")
    except Exception as e:
        logging.error(f"Failed to stop session with chargepoint: {chargepoint_id} and session id: {session_id}", exc_info=e)
