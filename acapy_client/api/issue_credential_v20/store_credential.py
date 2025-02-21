from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_cred_ex_record_detail import V20CredExRecordDetail
from ...models.v20_cred_store_request import V20CredStoreRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    cred_ex_id: str,
    json_body: V20CredStoreRequest,
) -> Dict[str, Any]:
    url = "{}/issue-credential-2.0/records/{cred_ex_id}/store".format(client.base_url, cred_ex_id=cred_ex_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20CredExRecordDetail]:
    if response.status_code == 200:
        response_200 = V20CredExRecordDetail.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20CredExRecordDetail]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    cred_ex_id: str,
    json_body: V20CredStoreRequest,
) -> Response[V20CredExRecordDetail]:
    kwargs = _get_kwargs(
        client=client,
        cred_ex_id=cred_ex_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    cred_ex_id: str,
    json_body: V20CredStoreRequest,
) -> Optional[V20CredExRecordDetail]:
    """ """

    return sync_detailed(
        client=client,
        cred_ex_id=cred_ex_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    cred_ex_id: str,
    json_body: V20CredStoreRequest,
) -> Response[V20CredExRecordDetail]:
    kwargs = _get_kwargs(
        client=client,
        cred_ex_id=cred_ex_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    cred_ex_id: str,
    json_body: V20CredStoreRequest,
) -> Optional[V20CredExRecordDetail]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            cred_ex_id=cred_ex_id,
            json_body=json_body,
        )
    ).parsed
