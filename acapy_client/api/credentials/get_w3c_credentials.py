from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.vc_record_list import VCRecordList
from ...models.w3c_credentials_list_request import W3CCredentialsListRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
    wql: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credentials/w3c".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "count": count,
        "start": start,
        "wql": wql,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[VCRecordList]:
    if response.status_code == 200:
        response_200 = VCRecordList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[VCRecordList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
    wql: Union[Unset, str] = UNSET,
) -> Response[VCRecordList]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        count=count,
        start=start,
        wql=wql,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
    wql: Union[Unset, str] = UNSET,
) -> Optional[VCRecordList]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        count=count,
        start=start,
        wql=wql,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
    wql: Union[Unset, str] = UNSET,
) -> Response[VCRecordList]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        count=count,
        start=start,
        wql=wql,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
    wql: Union[Unset, str] = UNSET,
) -> Optional[VCRecordList]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            count=count,
            start=start,
            wql=wql,
        )
    ).parsed
