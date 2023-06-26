from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.longship_error import LongshipError
from ...types import Response


def _get_kwargs(
    id: str,
    charge_point_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/locations/{id}/chargepoints/{chargePointId}".format(
        client.base_url, id=id, chargePointId=charge_point_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, LongshipError]]:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = LongshipError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = LongshipError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = LongshipError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LongshipError.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, LongshipError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    charge_point_id: str,
    *,
    client: Client,
) -> Response[Union[Any, LongshipError]]:
    """Deletes a relation between location and charge point.

     Deletes a relation between location and charge point.

    Args:
        id (str):
        charge_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LongshipError]]
    """

    kwargs = _get_kwargs(
        id=id,
        charge_point_id=charge_point_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    charge_point_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, LongshipError]]:
    """Deletes a relation between location and charge point.

     Deletes a relation between location and charge point.

    Args:
        id (str):
        charge_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LongshipError]
    """

    return sync_detailed(
        id=id,
        charge_point_id=charge_point_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    charge_point_id: str,
    *,
    client: Client,
) -> Response[Union[Any, LongshipError]]:
    """Deletes a relation between location and charge point.

     Deletes a relation between location and charge point.

    Args:
        id (str):
        charge_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LongshipError]]
    """

    kwargs = _get_kwargs(
        id=id,
        charge_point_id=charge_point_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    charge_point_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, LongshipError]]:
    """Deletes a relation between location and charge point.

     Deletes a relation between location and charge point.

    Args:
        id (str):
        charge_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LongshipError]
    """

    return (
        await asyncio_detailed(
            id=id,
            charge_point_id=charge_point_id,
            client=client,
        )
    ).parsed
