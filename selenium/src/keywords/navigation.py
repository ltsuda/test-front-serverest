from dataclasses import dataclass, field

from src import factory
from src.consts import Pages
from src.custom_selenium import CustomSelenium

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass(kw_only=True)
class Navigator:
    driver: WebDriver
    custom_selenium: CustomSelenium = field(init=False)

    def __post_init__(self):
        self.custom_selenium: CustomSelenium = CustomSelenium(self.driver)
        self.login_actions = factory.ActionsFactory.get(Pages.LOGIN, self.driver)
        self.register_actions = factory.ActionsFactory.get(Pages.REGISTER, self.driver)

    def _expect(self, url: str, *, should_assert: bool = True, should_wait: bool = True):
        at_url: bool = self.custom_selenium.url_to_be(url, should_wait=should_wait)
        if should_assert:
            assert at_url, f"Current page is not at {url}"

    def navigate_to_login(self, *, should_assert: bool = True, should_wait: bool = True):
        login_url: str = self.login_actions.goto()
        self._expect(login_url, should_assert=should_assert, should_wait=should_wait)

    def navigate_to_register(self, *, should_assert: bool = True, should_wait: bool = True):
        register_url: str = self.register_actions.goto()
        self._expect(register_url, should_assert=should_assert, should_wait=should_wait)
