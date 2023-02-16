from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from src.pom.ui.register.register import RegisterUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class RegisterQuery:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def is_register_as_administrator_selected(self) -> bool:
        return self.custom_selenium.find_element(
            RegisterUI.is_admin, should_wait=True
        ).is_selected()
