from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from src.pom.ui.common.alert import AlertUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AlertActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def close_alert(self, with_text: str):
        self.custom_selenium.find_element(AlertUI.close_button_locator(with_text)).click()
