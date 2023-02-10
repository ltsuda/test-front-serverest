from typing import Callable

import pytest
import requests
from consts import URL
from requests import Response
from requests.exceptions import HTTPError
from src.model.user import UserProtocol, UserWithID, UserWithIDProtocol


@pytest.fixture(scope="function")
def get_authorization_token(backend_url) -> Callable:
    def _login(email: str, password: str) -> str:
        response = None
        try:
            response = requests.post(
                f"{backend_url}{URL.login}",
                headers={"monitor": "false"},
                json={"email": email, "password": password},
            )
            response.raise_for_status()
        except HTTPError as http_err:
            if isinstance(response, Response):
                print(http_err)
            raise http_err
        assert response.status_code == 200
        token: str = response.json()["authorization"]
        return token

    return _login


@pytest.fixture(scope="function")
def create_account(backend_url) -> Callable:
    def _create_account(user: UserProtocol) -> UserWithIDProtocol:
        response = None
        try:
            response = requests.post(
                f"{backend_url}{URL.users}",
                headers={"monitor": "false"},
                data=user.data_as_dict(),
            )
            response.raise_for_status()
        except HTTPError as http_err:
            if isinstance(response, Response):
                print(response.text)
            raise http_err
        else:
            assert response.status_code == 201
            response_json = response.json()
            _id = response_json["_id"]
        return UserWithID(user.name, user.email, user.password, _id, user.as_admin)

    return _create_account
