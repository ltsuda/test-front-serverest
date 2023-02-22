from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from selenium.webdriver.remote.webdriver import WebDriver
from src.consts import URL
from src.pom.ui.register.register import RegisterUI


@dataclass(kw_only=True)
class RegisterActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def goto(self) -> str:
        register_url = f"{URL.base_url}{URL.register}"
        self.driver.get(register_url)
        return register_url

    def fill_name(self, name: str):
        self.custom_selenium.find_element(RegisterUI.name).send_keys(name)

    def fill_email(self, email: str):
        self.custom_selenium.find_element(RegisterUI.email).send_keys(email)

    def fill_password(self, password: str):
        self.custom_selenium.find_element(RegisterUI.password).send_keys(password)

    def click_login(self):
        self.custom_selenium.find_element(RegisterUI.login).click()

    def click_register(self):
        self.custom_selenium.find_element(RegisterUI.register).click()

    def select_as_administrator(self):
        element = self.custom_selenium.find_element(RegisterUI.is_admin)
        if not element.is_selected():
            element.click()

    def unselect_as_administrator(self):
        element = self.custom_selenium.find_element(RegisterUI.is_admin)
        if element.is_selected():
            element.click()
