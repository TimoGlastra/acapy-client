from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.post_transactions_conn_id_set_endorser_role_transaction_my_job import (
    PostTransactionsConnIdSetEndorserRoleTransactionMyJob,
)
from ...models.transaction_jobs import TransactionJobs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
    transaction_my_job: Union[Unset, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Dict[str, Any]:
    url = "{}/transactions/{conn_id}/set-endorser-role".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_transaction_my_job: Union[Unset, str] = UNSET
    if not isinstance(transaction_my_job, Unset):
        json_transaction_my_job = transaction_my_job.value

    params: Dict[str, Any] = {
        "transaction_my_job": json_transaction_my_job,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TransactionJobs]:
    if response.status_code == 200:
        response_200 = TransactionJobs.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TransactionJobs]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: str,
    transaction_my_job: Union[Unset, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Response[TransactionJobs]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        transaction_my_job=transaction_my_job,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    conn_id: str,
    transaction_my_job: Union[Unset, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Optional[TransactionJobs]:
    """ """

    return sync_detailed(
        client=client,
        conn_id=conn_id,
        transaction_my_job=transaction_my_job,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
    transaction_my_job: Union[Unset, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Response[TransactionJobs]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        transaction_my_job=transaction_my_job,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    conn_id: str,
    transaction_my_job: Union[Unset, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Optional[TransactionJobs]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            conn_id=conn_id,
            transaction_my_job=transaction_my_job,
        )
    ).parsed
