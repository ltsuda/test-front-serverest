from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from lean_pom.register_pom.register_pom import RegisterPOM

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class RegisterActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def fill_name(self, name: str):
        self.custom_selenium.find_element(RegisterPOM.name).send_keys(name)

    def fill_email(self, email: str):
        self.custom_selenium.find_element(RegisterPOM.email).send_keys(email)

    def fill_password(self, password: str):
        self.custom_selenium.find_element(RegisterPOM.password).send_keys(password)

    def click_login(self):
        self.custom_selenium.find_element(RegisterPOM.login).click()

    def click_register(self):
        self.custom_selenium.find_element(RegisterPOM.register).click()

    def select_as_administrator(self):
        element = self.custom_selenium.find_element(RegisterPOM.is_admin)
        if not element.is_selected():
            element.click()

    def unselect_as_administrator(self):
        element = self.custom_selenium.find_element(RegisterPOM.is_admin)
        if element.is_selected():
            element.click()

    def is_register_as_administrator_selected(self) -> bool:
        return self.custom_selenium.find_element(
            RegisterPOM.is_admin, should_wait=False
        ).is_selected()
