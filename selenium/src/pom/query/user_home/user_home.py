from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from src.pom.ui.user_home.user_home import UserHomeUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class UserHomeQuery:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def is_store_visible(self) -> bool:
        return self.custom_selenium.is_displayed(UserHomeUI.store, should_wait=True)
