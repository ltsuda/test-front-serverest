from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from src.pom.ui.admin_home.admin_home import AdminHomeUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AdminHomeQuery:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def has_welcome_message(self, for_user: str) -> bool:
        return self.custom_selenium.has_text(
            AdminHomeUI.welcome_selector, f"Bem Vindo {for_user}", strict=True, should_wait=False
        )

    def is_store_description_visible(self) -> bool:
        return self.custom_selenium.is_displayed(AdminHomeUI.store_description, should_wait=False)
