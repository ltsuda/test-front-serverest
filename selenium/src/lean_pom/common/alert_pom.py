from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(init=False)
class AlertPOM:
    _alert_selector: str = "//div[contains(@class, 'alert')]//span[text()='ERROR_MESSAGE']"
    _close_button_selector: str = "//button[@aria-label='Close']"

    @classmethod
    def _update_alert(cls, message: str) -> str:
        return cls._alert_selector.replace("ERROR_MESSAGE", message)

    @classmethod
    def alert_locator(cls, with_text: str) -> Locator:
        _alert_selector = cls._update_alert(with_text)
        return (By.XPATH, _alert_selector)

    @classmethod
    def close_button_locator(cls, with_text: str) -> Locator:
        button_selector = f"{cls._update_alert(with_text)}/..{cls._close_button_selector}"
        return (By.XPATH, button_selector)
