from dataclasses import dataclass, field

from src.custom_selenium import CustomSelenium
from src.pom.ui.admin_navbar.admin_navbar import AdminNavbarUI

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class AdminNavbarActions:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)

    def click_home(self):
        self.custom_selenium.find_element(AdminNavbarUI.home).click()

    def click_register_users(self):
        self.custom_selenium.find_element(AdminNavbarUI.register_users).click()

    def click_list_users(self):
        self.custom_selenium.find_element(AdminNavbarUI.list_users).click()

    def click_register_products(self):
        self.custom_selenium.find_element(AdminNavbarUI.register_products).click()

    def click_list_products(self):
        self.custom_selenium.find_element(AdminNavbarUI.list_products).click()

    def click_reports(self):
        self.custom_selenium.find_element(AdminNavbarUI.register_products).click()

    def click_logout(self):
        self.custom_selenium.find_element(AdminNavbarUI.logout).click()
