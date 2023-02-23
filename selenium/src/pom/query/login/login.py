from dataclasses import dataclass, field

from src.custom_selenium import CustomSelenium
from src.pom.query.common.alert import AlertQuery

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class LoginQuery:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)
    alert: AlertQuery = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)
        self.alert: AlertQuery = AlertQuery(driver=self.driver)
