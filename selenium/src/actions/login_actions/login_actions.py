from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from lean_pom.login_pom.login_pom import LoginPOM

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class LoginActions:
    driver: WebDriver
    login_pom: LoginPOM = LoginPOM()
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def fill_email(self, email: str):
        self.custom_selenium.find_element(LoginPOM.email).send_keys(email)

    def fill_password(self, password: str):
        self.custom_selenium.find_element(LoginPOM.password).send_keys(password)

    def click_login(self):
        self.custom_selenium.find_element(LoginPOM.login).click()

    def click_register(self):
        self.custom_selenium.find_element(LoginPOM.register).click()
