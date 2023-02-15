from contextlib import contextmanager
from typing import Generator, LiteralString

import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait

# Selenium locator (By.identifier, 'selector')
Locator = tuple[LiteralString, str]


class CustomSelenium:
    """Selenium helper class

    NOTE: This class is probably not a best practice
    """

    default_explicit_timeout: int = 60

    def __init__(self, driver: WebDriver) -> None:
        self._driver: WebDriver = driver
        self._explicit_wait_timeout: int = self.default_explicit_timeout

    @contextmanager
    def toggle_explicit_timeout(self, should_wait: bool = True) -> Generator:
        """Context Manager to toggle instance explicit_wait_timeout value

        Args:
            should_wait (bool, optional): Whether keep explicit timeout or zero out.
            Defaults to True.

        Yields:
            Generator: Just yields
        """

        def set_explicit_wait(timeout: int) -> None:
            """Local function to set instance explicit_wait_timeout value if should_wait is False

            Args:
                timeout (int): time in seconds
            """
            if not should_wait:
                print(f"Setting explicit_wait_timeout to {timeout}")
                self._explicit_wait_timeout = timeout

        set_explicit_wait(0)
        yield
        set_explicit_wait(self._explicit_wait_timeout)

    def find_element(self, locator: Locator, *, should_wait: bool = True) -> WebElement:
        """Find Selenium Webelement with explicit wait

        Args:
            locator (Locator): Selenium locator tuple (By.identifier, selector)
            should_wait (bool, optional): Whether to use wait until is visible. Defaults to True.

        Returns:
            WebElement: Selenium's web element
        """
        with self.toggle_explicit_timeout(should_wait):
            return wait.WebDriverWait(self._driver, self._explicit_wait_timeout).until(
                EC.visibility_of_element_located(locator)
            )

    def is_displayed(self, locator: Locator, *, should_wait: bool = True) -> bool:  # type: ignore
        """Check if element is displayed

        It will try to wait to element to be present but not visible, then uses Selenium's function
        to check if it's displayed. If element is not present, returns False.

        Args:
            locator (Locator): Selenium locator tuple (By.identifier, selector)
            should_wait (bool, optional): Whether to use wait until is visible. Defaults to True.

        Returns:
            bool: if element is displayed or not
        """
        with self.toggle_explicit_timeout(should_wait):
            try:
                element: WebElement = wait.WebDriverWait(
                    self._driver, self._explicit_wait_timeout
                ).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                return False
            else:
                return element.is_displayed()
