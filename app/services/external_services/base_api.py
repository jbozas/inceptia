import requests
import typing
from fastapi import HTTPException, HTTPException
from abc import ABC


class BaseService(ABC):
    """Base service to communicate with any Backend."""

    client = requests

    @classmethod
    def _request(
        self,
        method: str,
        url: str,
        *,
        headers: dict = {},
        json: typing.Any | None = None,
        data: typing.Any | None = None,
        auth: typing.Any | None = None,
        params: dict | None = None,
    ) -> typing.Any:

        result = self.client.request(
            method=method,
            url=url,
            json=json,
            data=data,
            headers=headers,
            auth=auth,
            params=params,
        )

        if not result.ok:
            raise HTTPException(
                result.status_code, f"Err {result.status_code} calling to {url}"
            )

        result.raise_for_status()
        return result.json() if result.content else None

    @classmethod
    def _get(
        self,
        url: str,
        headers: dict = {},
        params: dict | None = None,
        auth=None,
        data: typing.Any | None = None,
    ) -> typing.Any:
        return self._request(
            "GET", url, headers=headers, data=data, auth=auth, params=params
        )
