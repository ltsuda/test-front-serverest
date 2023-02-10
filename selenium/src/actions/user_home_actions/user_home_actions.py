from dataclasses import dataclass, field

from custom_selenium import CustomSelenium
from lean_pom.user_home_pom.user_home_pom import UserHomePOM

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class UserHomeActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def fill_search(self, product: str):
        self.custom_selenium.find_element(UserHomePOM.search_field).send_keys(product)

    def click_search(self):
        self.custom_selenium.find_element(UserHomePOM.search_button).click()

    def is_store_visible(self) -> bool:
        return self.custom_selenium.is_displayed(UserHomePOM.store, should_wait=False)
