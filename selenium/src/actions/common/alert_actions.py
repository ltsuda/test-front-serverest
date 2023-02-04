from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from lean_pom.common.alert_pom import AlertPOM

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


@dataclass(kw_only=True)
class AlertActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def _alert(self, with_text: str) -> WebElement:
        return self.custom_selenium.find_element(AlertPOM.alert_locator(with_text))

    def _close_button(self, alert_text: str) -> WebElement:
        return self.custom_selenium.find_element(AlertPOM.close_button_locator(alert_text))

    def is_alert_visible(self, with_text: str) -> bool:
        return self._alert(with_text).is_displayed()

    def close_alert(self, with_text: str):
        self._close_button(with_text).click()
