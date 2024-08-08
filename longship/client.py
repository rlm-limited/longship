from longship_api_client.client import Client


class LongshipClient:

    def __init__(self, base_url: str, apiKey: str, ocpKey: str, token_group_id: str) -> None:
        self.client = Client(base_url=base_url).with_headers({"x-api-key": apiKey, "Ocp-Apim-Subscription-Key": ocpKey})
        self.token_group_id = token_group_id
