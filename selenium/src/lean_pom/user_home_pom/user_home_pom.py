from dataclasses import dataclass

from custom_selenium import Locator

from selenium.webdriver.common.by import By


@dataclass(frozen=True, init=False)
class UserHomePOM:
    store: Locator = (By.XPATH, "//h1[text()='Serverest Store']")
    search_field: Locator = (By.CSS_SELECTOR, "[data-testid='pesquisar']")
    search_button: Locator = (By.CSS_SELECTOR, "[data-testid='botaoPesquisar']")
