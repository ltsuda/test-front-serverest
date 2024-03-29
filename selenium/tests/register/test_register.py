import typing

import pytest
from src import factory
from src.consts import URL, Pages
from src.keywords.navigator import Navigator

if typing.TYPE_CHECKING:
    from src.pom.actions.register_actions.register import RegisterActions
    from src.pom.query.admin_home.admin_home import AdminHomeQuery
    from src.pom.query.register.register import RegisterQuery
    from src.pom.query.user_home.user_home import UserHomeQuery

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.register
class TestRegister:
    @pytest.mark.register_001
    def test_admin_register_redirected_to_home(self, driver: WebDriver, admin_user):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _admin_home: AdminHomeQuery = factory.QueriesFactory.get(
            Pages.ADMIN_HOME, driver=driver  # type: ignore
        )
        admin_data = admin_user.data()
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name(admin_data.name)
        _register_actions.fill_email(admin_data.email)
        _register_actions.fill_password(admin_data.password)
        _register_actions.select_as_administrator()
        assert _register_query.is_register_as_administrator_selected()
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Cadastro realizado com sucesso")
        assert navigator.url_contains("admin")
        assert _admin_home.has_welcome_message(for_user=admin_data.name)
        assert _admin_home.is_store_description_visible()

    @pytest.mark.register_002
    def test_user__register_redirected_to_home(self, driver: WebDriver, regular_user):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _user_home: UserHomeQuery = factory.QueriesFactory.get(
            Pages.USER_HOME, driver=driver  # type: ignore
        )
        user_data = regular_user.data()
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name(user_data.name)
        _register_actions.fill_email(user_data.email)
        _register_actions.fill_password(user_data.password)
        assert _register_query.is_register_as_administrator_selected() is False
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Cadastro realizado com sucesso")
        assert _user_home.is_store_visible()
        assert navigator.url_contains("admin") is False

    @pytest.mark.register_003
    def test_redirected_to_login(self, driver: WebDriver):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.click_login()

        assert navigator.url_to_be(f"{URL.base_url}{URL.login}", should_assert=False)

    @pytest.mark.register_004
    def test_alert_register_name_is_required(self, driver: WebDriver):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_email("user@provider.com")
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Nome é obrigatório")

    @pytest.mark.register_005
    def test_alert_register_email_is_required(self, driver: WebDriver):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Email é obrigatório")

    @pytest.mark.register_006
    def test_alert_register_password_is_required(self, driver: WebDriver):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_email("user@provider.com")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Password é obrigatório")

    @pytest.mark.register_007
    def test_alert_email_already_in_use(self, driver: WebDriver, user_account):
        _register_actions: RegisterActions = factory.ActionsFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        _register_query: RegisterQuery = factory.QueriesFactory.get(
            Pages.REGISTER, driver  # type: ignore
        )
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_email(user_account.email)
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Este email já está sendo usado")
