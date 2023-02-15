from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(frozen=True, init=False)
class LoginUI:
    email: Locator = (By.CSS_SELECTOR, "[data-testid='email']")
    password: Locator = (By.CSS_SELECTOR, "[data-testid='senha']")
    login: Locator = (By.CSS_SELECTOR, "[data-testid='entrar']")
    register: Locator = (By.CSS_SELECTOR, "[data-testid='cadastrar']")
