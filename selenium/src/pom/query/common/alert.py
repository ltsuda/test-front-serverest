from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from src.pom.ui.common.alert import AlertUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AlertQuery:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def is_alert_visible(self, with_text: str) -> bool:
        return self.custom_selenium.is_displayed(
            AlertUI.alert_locator(with_text), should_wait=False
        )
