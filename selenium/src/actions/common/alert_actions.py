from dataclasses import dataclass, field

import allure
from custom_selenium import CustomSelenium
from lean_pom.common.alert_pom import AlertPOM

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AlertActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    @allure.step
    def is_alert_visible(self, with_text: str) -> bool:
        return self.custom_selenium.is_displayed(
            AlertPOM.alert_locator(with_text), should_wait=False
        )

    @allure.step
    def close_alert(self, with_text: str):
        self.custom_selenium.find_element(AlertPOM.close_button_locator(with_text)).click()
