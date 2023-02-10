from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from lean_pom.admin_home_pom.admin_home_pom import AdminHomePOM

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AdminHomeActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def is_welcome_visible(self, for_user: str) -> bool:
        return self.custom_selenium.is_displayed(
            AdminHomePOM.welcome_locator(for_user), should_wait=False
        )

    def is_store_description_visible(self) -> bool:
        return self.custom_selenium.is_displayed(AdminHomePOM.store_description, should_wait=False)
