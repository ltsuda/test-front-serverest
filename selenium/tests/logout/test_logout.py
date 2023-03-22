import typing

import pytest
from src import factory
from src.consts import URL, Pages

if typing.TYPE_CHECKING:
    from src.pom.actions.admin_home_actions.admin_home import AdminHomeActions

from src.keywords.navigator import Navigator
from src.keywords.auth import authenticate
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.logout
class TestLogout:
    @pytest.mark.logout_001
    def test_admin_logout(self, driver: WebDriver, admin_account):
        auth_driver = authenticate(
            driver, admin_account.name, admin_account.email, admin_account.password
        )
        _navigator = Navigator(driver=driver)
        _admin_home_actions: AdminHomeActions = factory.ActionsFactory.get(  # type: ignore
            Pages.ADMIN_HOME, auth_driver
        )

        _navigator.navigate_to_admin_home(should_assert=True)

        _admin_home_actions.navbar.click_logout()
        assert _navigator.url_to_be(f"{URL.base_url}{URL.login}", should_assert=False)
