from selenium.webdriver.remote.webdriver import WebDriver
import requests
from requests.exceptions import HTTPError
from consts import URL
from requests import Response


def api_login(email: str, password: str, *, backend_url=URL.external_backend) -> str:
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


def authenticate(driver: WebDriver, name: str, email: str, password: str):
    token = api_login(email, password)

    local_storage = {
        "serverest/userNome": name,
        "serverest/userEmail": email,
        "serverest/userToken": token,
    }
    set_local_storage_script = """
        (storage => {
            for (const [key, value] of Object.entries(storage)) {
                if (storage.hasOwnProperty(key)) {
                    window.localStorage.setItem(key, value)
                }
            }
        })(arguments[0])
    """
    driver.execute_script(set_local_storage_script, local_storage)
    return driver
