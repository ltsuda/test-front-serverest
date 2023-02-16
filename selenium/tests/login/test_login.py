import uuid

import pytest
import src.pom.actions.login_actions.login as login_actions
import src.pom.query.admin_home.admin_home as admin_home
import src.pom.query.common.alert as alert_query
import src.pom.query.user_home.user_home as user_home
from src.consts import URL

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.login
class TestLogin:
    @pytest.mark.login_001
    def test_admin_redirected_to_home(self, driver: WebDriver, admin_account):
        _login_action = login_actions.LoginActions(driver=driver)
        _admin_home = admin_home.AdminHomeQuery(driver=driver)

        _login_action.fill_email(admin_account.email)
        _login_action.fill_password(admin_account.password)
        _login_action.click_login()

        assert "admin" in driver.current_url
        assert _admin_home.has_welcome_message(for_user=admin_account.name)
        assert _admin_home.is_store_description_visible()

    @pytest.mark.login_002
    def test_user_redirected_to_home(self, driver: WebDriver, user_account):
        _login_action = login_actions.LoginActions(driver=driver)
        _user_home = user_home.UserHomeQuery(driver=driver)

        _login_action.fill_email(user_account.email)
        _login_action.fill_password(user_account.password)
        _login_action.click_login()

        assert "admin" not in driver.current_url
        assert _user_home.is_store_visible()

    @pytest.mark.login_003
    def test_redirected_to_register(self, driver: WebDriver, base_url):
        _login_actions = login_actions.LoginActions(driver=driver)

        _login_actions.click_register()

        assert driver.current_url == f"{base_url}{URL.register}"

    @pytest.mark.login_004
    def test_alert_email_is_required(self, driver: WebDriver):
        _login_actions = login_actions.LoginActions(driver=driver)
        _alert_query = alert_query.AlertQuery(driver=driver)

        _login_actions.fill_password("password")
        _login_actions.click_login()

        assert _alert_query.is_alert_visible(with_text="Email é obrigatório")

    @pytest.mark.login_005
    def test_alert_password_is_required(self, driver: WebDriver):
        _login_actions = login_actions.LoginActions(driver=driver)
        _alert_query = alert_query.AlertQuery(driver=driver)

        _login_actions.fill_email("user@provider.com")
        _login_actions.click_login()

        assert _alert_query.is_alert_visible(with_text="Password é obrigatório")

    @pytest.mark.login_006
    def test_alert_email_not_registered(self, driver: WebDriver):
        _login_actions = login_actions.LoginActions(driver=driver)
        _alert_query = alert_query.AlertQuery(driver=driver)

        _login_actions.fill_email(f"{uuid.uuid4()}@provider.com")
        _login_actions.fill_password("password")
        _login_actions.click_login()

        assert _alert_query.is_alert_visible(with_text="Email e/ou senha inválidos")

    @pytest.mark.login_007
    def test_alert_invalid_credentials(self, driver: WebDriver, user_account):
        _login_actions = login_actions.LoginActions(driver=driver)
        _alert_query = alert_query.AlertQuery(driver=driver)

        _login_actions.fill_email(user_account.email)
        _login_actions.fill_password(f"{uuid.uuid4()}")
        _login_actions.click_login()

        assert _alert_query.is_alert_visible(with_text="Email e/ou senha inválidos")
