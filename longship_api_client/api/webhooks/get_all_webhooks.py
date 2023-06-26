from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_all_webhooks_order_by import GetAllWebhooksOrderBy
from ...models.longship_error import LongshipError
from ...models.webhook_summary_get_dto import WebhookSummaryGetDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    take: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, GetAllWebhooksOrderBy] = GetAllWebhooksOrderBy.NAME,
    descending: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/webhooks".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["skip"] = skip

    params["take"] = take

    params["search"] = search

    json_order_by: Union[Unset, None, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value if order_by else None

    params["orderBy"] = json_order_by

    params["descending"] = descending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemaswebhook_summary_get_dto_array_item_data in _response_200:
            componentsschemaswebhook_summary_get_dto_array_item = WebhookSummaryGetDto.from_dict(
                componentsschemaswebhook_summary_get_dto_array_item_data
            )

            response_200.append(componentsschemaswebhook_summary_get_dto_array_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = LongshipError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = LongshipError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LongshipError.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    take: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, GetAllWebhooksOrderBy] = GetAllWebhooksOrderBy.NAME,
    descending: Union[Unset, None, bool] = UNSET,
) -> Response[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    """Get a list of webhooks.

     Get a paged list of webhooks, taken the filters into account.

    Args:
        skip (Union[Unset, None, int]):
        take (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        order_by (Union[Unset, None, GetAllWebhooksOrderBy]):  Default:
            GetAllWebhooksOrderBy.NAME.
        descending (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['WebhookSummaryGetDto'], LongshipError]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        take=take,
        search=search,
        order_by=order_by,
        descending=descending,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    take: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, GetAllWebhooksOrderBy] = GetAllWebhooksOrderBy.NAME,
    descending: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    """Get a list of webhooks.

     Get a paged list of webhooks, taken the filters into account.

    Args:
        skip (Union[Unset, None, int]):
        take (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        order_by (Union[Unset, None, GetAllWebhooksOrderBy]):  Default:
            GetAllWebhooksOrderBy.NAME.
        descending (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['WebhookSummaryGetDto'], LongshipError]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        take=take,
        search=search,
        order_by=order_by,
        descending=descending,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    take: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, GetAllWebhooksOrderBy] = GetAllWebhooksOrderBy.NAME,
    descending: Union[Unset, None, bool] = UNSET,
) -> Response[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    """Get a list of webhooks.

     Get a paged list of webhooks, taken the filters into account.

    Args:
        skip (Union[Unset, None, int]):
        take (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        order_by (Union[Unset, None, GetAllWebhooksOrderBy]):  Default:
            GetAllWebhooksOrderBy.NAME.
        descending (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['WebhookSummaryGetDto'], LongshipError]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        take=take,
        search=search,
        order_by=order_by,
        descending=descending,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    take: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, GetAllWebhooksOrderBy] = GetAllWebhooksOrderBy.NAME,
    descending: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[List["WebhookSummaryGetDto"], LongshipError]]:
    """Get a list of webhooks.

     Get a paged list of webhooks, taken the filters into account.

    Args:
        skip (Union[Unset, None, int]):
        take (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        order_by (Union[Unset, None, GetAllWebhooksOrderBy]):  Default:
            GetAllWebhooksOrderBy.NAME.
        descending (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['WebhookSummaryGetDto'], LongshipError]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            take=take,
            search=search,
            order_by=order_by,
            descending=descending,
        )
    ).parsed
