import pytest
import src.pom.actions.register_actions.register as register_actions
import src.pom.query.admin_home.admin_home as admin_home
import src.pom.query.register.register as register_query
import src.pom.query.user_home.user_home as user_home
from src.consts import URL
from src.keywords.navigation import Navigator

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.register
class TestLogin:
    @pytest.mark.register_001
    def test_admin_register_redirected_to_home(self, driver: WebDriver, admin_user):
        _register_action = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        _admin_home = admin_home.AdminHomeQuery(driver=driver)
        admin_data = admin_user.data()
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_action.fill_name(admin_data.name)
        _register_action.fill_email(admin_data.email)
        _register_action.fill_password(admin_data.password)
        _register_action.select_as_administrator()
        assert _register_query.is_register_as_administrator_selected()
        _register_action.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Cadastro realizado com sucesso")
        assert _admin_home.has_welcome_message(for_user=admin_data.name)
        assert _admin_home.is_store_description_visible()
        assert "admin" in driver.current_url

    @pytest.mark.register_002
    def test_user__register_redirected_to_home(self, driver: WebDriver, regular_user):
        _register_action = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        _user_home = user_home.UserHomeQuery(driver=driver)
        user_data = regular_user.data()
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_action.fill_name(user_data.name)
        _register_action.fill_email(user_data.email)
        _register_action.fill_password(user_data.password)
        assert _register_query.is_register_as_administrator_selected() is False
        _register_action.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Cadastro realizado com sucesso")
        assert _user_home.is_store_visible()
        assert "admin" not in driver.current_url

    @pytest.mark.register_003
    def test_redirected_to_login(self, driver: WebDriver):
        _register_actions = register_actions.RegisterActions(driver=driver)
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.click_login()

        assert navigator.driver.current_url == f"{URL.base_url}{URL.login}"

    @pytest.mark.register_004
    def test_alert_register_name_is_required(self, driver: WebDriver):
        _register_actions = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_email("user@provider.com")
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Nome é obrigatório")

    @pytest.mark.register_005
    def test_alert_register_email_is_required(self, driver: WebDriver):
        _register_actions = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Email é obrigatório")

    @pytest.mark.register_006
    def test_alert_register_password_is_required(self, driver: WebDriver):
        _register_actions = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_email("user@provider.com")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Password é obrigatório")

    @pytest.mark.register_007
    def test_alert_email_already_in_use(self, driver: WebDriver, user_account):
        _register_actions = register_actions.RegisterActions(driver=driver)
        _register_query = register_query.RegisterQuery(driver=driver)
        navigator = Navigator(driver=driver)
        navigator.navigate_to_register()

        _register_actions.fill_name("John Doe")
        _register_actions.fill_email(user_account.email)
        _register_actions.fill_password("password")
        _register_actions.click_register()

        assert _register_query.alert.is_alert_visible(with_text="Este email já está sendo usado")
