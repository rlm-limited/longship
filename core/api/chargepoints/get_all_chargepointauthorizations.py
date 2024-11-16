from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import Unset
import datetime
from ...models.longship_error import LongshipError
from ...models.charge_point_authorize_get_dto import ChargePointAuthorizeGetDto


def _get_kwargs(
    id: str,
    *,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    descending: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    take: Union[Unset, int] = UNSET,
    idtag: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["descending"] = descending

    params["status"] = status

    params["search"] = search

    params["skip"] = skip

    params["take"] = take

    params["idtag"] = idtag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/chargepoints/{id}/authorization".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for (
            componentsschemascharge_point_authorize_get_dto_array_item_data
        ) in _response_200:
            componentsschemascharge_point_authorize_get_dto_array_item = (
                ChargePointAuthorizeGetDto.from_dict(
                    componentsschemascharge_point_authorize_get_dto_array_item_data
                )
            )

            response_200.append(
                componentsschemascharge_point_authorize_get_dto_array_item
            )

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = LongshipError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = LongshipError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = LongshipError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LongshipError.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    descending: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    take: Union[Unset, int] = UNSET,
    idtag: Union[Unset, str] = UNSET,
) -> Response[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    """Get a list of chargepointauthorizations.

     Get a paged list of chargepointauthorizations, taken the filters into account.

    Args:
        id (str):
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        descending (Union[Unset, bool]):
        status (Union[Unset, str]):
        search (Union[Unset, str]):
        skip (Union[Unset, int]):
        take (Union[Unset, int]):
        idtag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ChargePointAuthorizeGetDto'], LongshipError]]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        descending=descending,
        status=status,
        search=search,
        skip=skip,
        take=take,
        idtag=idtag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    descending: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    take: Union[Unset, int] = UNSET,
    idtag: Union[Unset, str] = UNSET,
) -> Optional[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    """Get a list of chargepointauthorizations.

     Get a paged list of chargepointauthorizations, taken the filters into account.

    Args:
        id (str):
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        descending (Union[Unset, bool]):
        status (Union[Unset, str]):
        search (Union[Unset, str]):
        skip (Union[Unset, int]):
        take (Union[Unset, int]):
        idtag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ChargePointAuthorizeGetDto'], LongshipError]
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
        descending=descending,
        status=status,
        search=search,
        skip=skip,
        take=take,
        idtag=idtag,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    descending: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    take: Union[Unset, int] = UNSET,
    idtag: Union[Unset, str] = UNSET,
) -> Response[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    """Get a list of chargepointauthorizations.

     Get a paged list of chargepointauthorizations, taken the filters into account.

    Args:
        id (str):
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        descending (Union[Unset, bool]):
        status (Union[Unset, str]):
        search (Union[Unset, str]):
        skip (Union[Unset, int]):
        take (Union[Unset, int]):
        idtag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ChargePointAuthorizeGetDto'], LongshipError]]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        descending=descending,
        status=status,
        search=search,
        skip=skip,
        take=take,
        idtag=idtag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    descending: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    take: Union[Unset, int] = UNSET,
    idtag: Union[Unset, str] = UNSET,
) -> Optional[Union[List["ChargePointAuthorizeGetDto"], LongshipError]]:
    """Get a list of chargepointauthorizations.

     Get a paged list of chargepointauthorizations, taken the filters into account.

    Args:
        id (str):
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        descending (Union[Unset, bool]):
        status (Union[Unset, str]):
        search (Union[Unset, str]):
        skip (Union[Unset, int]):
        take (Union[Unset, int]):
        idtag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ChargePointAuthorizeGetDto'], LongshipError]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
            descending=descending,
            status=status,
            search=search,
            skip=skip,
            take=take,
            idtag=idtag,
        )
    ).parsed
