from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(frozen=True, init=False)
class AdminHomeUI:
    welcome_selector: Locator = (By.XPATH, "//h1[contains(text(), 'Bem Vindo')]")
    store_description: Locator = (
        By.XPATH,
        "//p[text()='Este é seu sistema para administrar seu ecommerce.']",
    )
