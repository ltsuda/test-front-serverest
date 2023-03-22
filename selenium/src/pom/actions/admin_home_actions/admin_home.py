from dataclasses import dataclass, field

from src.consts import URL
from src.custom_selenium import CustomSelenium
from src.pom.actions.admin_navbar_actions.admin_navbar import AdminNavbarActions
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AdminHomeActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)
    navbar: AdminNavbarActions = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)
        self.navbar: AdminNavbarActions = AdminNavbarActions(driver=self.driver)

    def goto(self) -> str:
        admin_home_url = f"{URL.base_url}{URL.admin_home}"
        self.driver.get(admin_home_url)
        return admin_home_url
