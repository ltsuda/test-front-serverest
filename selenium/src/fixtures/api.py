from typing import Callable

import pytest
import requests
from consts import URL
from requests import Response
from requests.exceptions import HTTPError
from src.model.user import UserProtocol


@pytest.fixture(scope="function")
def get_authorization_token_for(base_url) -> Callable:
    def _login(email: str, password: str) -> str | None:
        token = None
        response = None
        try:
            response = requests.post(
                f"{base_url}{URL.login}",
                headers={"monitor": "false"},
                json={"email": email, "password": password},
            )
            response.raise_for_status()
        except HTTPError as http_err:
            if isinstance(response, Response):
                print(http_err)
            raise http_err
        else:
            assert response.status_code == 200
            token = response.json()["authorization"]
        return token

    return _login


@pytest.fixture(scope="function")
def create_account_for(base_url) -> Callable:
    def _create_account(user: UserProtocol) -> dict:
        response = None
        account = {
            "nome": user.name,
            "email": user.email,
            "password": user.password,
            "administrador": "true" if user.as_admin else "false",
        }
        try:
            response = requests.post(
                f"{base_url}{URL.users}", headers={"monitor": "false"}, data=account
            )
            response.raise_for_status()
        except HTTPError as http_err:
            if isinstance(response, Response):
                print(response.text)
            raise http_err
        else:
            assert response.status_code == 201
            response_json = response.json()
            account["_id"] = response_json["_id"]
        return account

    return _create_account
