import typing
import uuid

import pytest
from src import factory
from src.consts import URL, Pages

if typing.TYPE_CHECKING:
    from src.pom.actions.login_actions.login import LoginActions
    from src.pom.query.admin_home.admin_home import AdminHomeQuery
    from src.pom.query.login.login import LoginQuery
    from src.pom.query.user_home.user_home import UserHomeQuery

from src.keywords.navigator import Navigator

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.login
class TestLogin:
    @pytest.mark.login_001
    def test_admin_redirected_to_home(self, driver: WebDriver, admin_account):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _admin_home: AdminHomeQuery = factory.QueriesFactory.get(
            Pages.ADMIN_HOME, driver=driver  # type: ignore
        )
        navigator = Navigator(driver=driver)

        _login_actions.fill_email(admin_account.email)
        _login_actions.fill_password(admin_account.password)
        _login_actions.click_login()

        assert navigator.url_contains("admin")
        assert _admin_home.has_welcome_message(for_user=admin_account.name)
        assert _admin_home.is_store_description_visible()

    @pytest.mark.login_002
    def test_user_redirected_to_home(self, driver: WebDriver, user_account):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _user_home: UserHomeQuery = factory.QueriesFactory.get(
            Pages.USER_HOME, driver=driver  # type: ignore
        )
        navigator = Navigator(driver=driver)

        _login_actions.fill_email(user_account.email)
        _login_actions.fill_password(user_account.password)
        _login_actions.click_login()

        assert navigator.url_contains("admin") is False
        assert _user_home.is_store_visible()

    @pytest.mark.login_003
    def test_redirected_to_register(self, driver: WebDriver):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        navigator = Navigator(driver=driver)

        _login_actions.click_register()

        assert navigator.url_to_be(f"{URL.base_url}{URL.register}", should_assert=False)

    @pytest.mark.login_004
    def test_alert_email_is_required(self, driver: WebDriver):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _login_query: LoginQuery = factory.QueriesFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )

        _login_actions.fill_password("password")
        _login_actions.click_login()

        assert _login_query.alert.is_alert_visible(with_text="Email é obrigatório")

    @pytest.mark.login_005
    def test_alert_password_is_required(self, driver: WebDriver):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _login_query: LoginQuery = factory.QueriesFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )

        _login_actions.fill_email("user@provider.com")
        _login_actions.click_login()

        assert _login_query.alert.is_alert_visible(with_text="Password é obrigatório")

    @pytest.mark.login_006
    def test_alert_email_not_registered(self, driver: WebDriver):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _login_query: LoginQuery = factory.QueriesFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )

        _login_actions.fill_email(f"{uuid.uuid4()}@provider.com")
        _login_actions.fill_password("password")
        _login_actions.click_login()

        assert _login_query.alert.is_alert_visible(with_text="Email e/ou senha inválidos")

    @pytest.mark.login_007
    def test_alert_invalid_credentials(self, driver: WebDriver, user_account):
        _login_actions: LoginActions = factory.ActionsFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )
        _login_query: LoginQuery = factory.QueriesFactory.get(
            Pages.LOGIN, driver=driver  # type: ignore
        )

        _login_actions.fill_email(user_account.email)
        _login_actions.fill_password(f"{uuid.uuid4()}")
        _login_actions.click_login()

        assert _login_query.alert.is_alert_visible(with_text="Email e/ou senha inválidos")
