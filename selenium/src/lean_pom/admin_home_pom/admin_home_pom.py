from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(frozen=True, init=False)
class AdminHomePOM:
    _welcome_selector: str = "//h1[text()='Bem vindo  USER_NAME']"
    store_description: Locator = (
        By.XPATH,
        "//p[text()='Este é seu sistema para administrar seu ecommerce.']",
    )

    @classmethod
    def welcome_locator(cls, name: str) -> Locator:
        _welcome_selector = cls._welcome_selector.replace("USER_NAME", name)
        return (By.XPATH, _welcome_selector)
