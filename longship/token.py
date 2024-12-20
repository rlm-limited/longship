from core.api.localtokengroupstoken import local_token_group_token_post
from core.models.local_token_group_token_post_dto import LocalTokenGroupTokenPostDto
from longship.client import LongshipClient
from longship.errors import CreateTokenError
import json


def create_token(client: LongshipClient, id: str, name: str | None = None) -> LocalTokenGroupTokenPostDto:
    response = local_token_group_token_post.sync_detailed(id=client.token_group_id, body=LocalTokenGroupTokenPostDto(uid=id, name=name, is_valid=True), client=client.client)
    if response.status_code.value == 201 or response.status_code.value == 409:
        return LocalTokenGroupTokenPostDto(is_valid=True, uid=id, name=name)
    raise CreateTokenError(f"Failed to create token group token: {json.loads(response.content.decode("utf-8"))['errorDetails']['message']}")
