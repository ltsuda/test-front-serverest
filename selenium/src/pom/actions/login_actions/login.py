from dataclasses import dataclass, field

from src.consts import URL
from src.custom_selenium import CustomSelenium
from src.pom.actions.common.alert import AlertActions
from src.pom.ui.login.login import LoginUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class LoginActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)
    alert: AlertActions = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)
        self.alert: AlertActions = AlertActions(driver=self.driver)

    def goto(self) -> str:
        login_url = f"{URL.base_url}{URL.login}"
        self.driver.get(login_url)
        return login_url

    def fill_email(self, email: str):
        self.custom_selenium.find_element(LoginUI.email).send_keys(email)

    def fill_password(self, password: str):
        self.custom_selenium.find_element(LoginUI.password).send_keys(password)

    def click_login(self):
        self.custom_selenium.find_element(LoginUI.login).click()

    def click_register(self):
        self.custom_selenium.find_element(LoginUI.register).click()
