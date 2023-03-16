from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(frozen=True, init=False)
class AdminNavbarUI:
    home: Locator = (By.CSS_SELECTOR, "[data-testid='home']")
    register_users: Locator = (By.CSS_SELECTOR, "[data-testid='cadastrar-usuarios']")
    list_users: Locator = (By.CSS_SELECTOR, "[data-testid='listar-usuarios']")
    register_products: Locator = (By.CSS_SELECTOR, "[data-testid='cadastrar-produtos']")
    list_products: Locator = (By.CSS_SELECTOR, "[data-testid='listar-produtos']")
    reports: Locator = (By.CSS_SELECTOR, "[data-testid='link-relatorios']")
    logout: Locator = (By.CSS_SELECTOR, "[data-testid='logout']")
