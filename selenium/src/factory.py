from src.consts import Pages
from src.pom.actions.login_actions import login as login_actions
from src.pom.actions.register_actions import register as register_actions
from src.pom.actions.admin_home_actions import admin_home as admin_home_actions
from src.pom.query.admin_home import admin_home as admin_home_query
from src.pom.query.login import login as login_query
from src.pom.query.register import register as register_query
from src.pom.query.user_home import user_home as home_query
from selenium.webdriver.remote.webdriver import WebDriver


class ActionsFactory:
    """Class representing Actions Factory for pages"""

    @staticmethod
    def get(for_page: str, driver: WebDriver):
        """Get the correct page action class instance

        Args:
            for_page (str): desired page name. See class Pages in consts.py to see the available
            values
            driver (WebDriver): Selenium webdriver instance

        Returns:
            class: a new instance of the selected actions page class
        """
        match for_page:
            case Pages.LOGIN:
                return login_actions.LoginActions(driver=driver)
            case Pages.REGISTER:
                return register_actions.RegisterActions(driver=driver)
            case Pages.ADMIN_HOME:
                return admin_home_actions.AdminHomeActions(driver=driver)
            case _:
                return login_actions.LoginActions(driver=driver)


class QueriesFactory:
    """Class representing Query Factory for pages"""

    @staticmethod
    def get(for_page: str, driver: WebDriver):
        """Get the correct page query class instance

        Args:
            for_page (str): desired page name. See class Pages in consts.py to see the available
            values
            driver (WebDriver): Selenium webdriver instance

        Returns:
            class: a new instance of the selected query page class
        """
        match for_page:
            case Pages.LOGIN:
                return login_query.LoginQuery(driver=driver)
            case Pages.REGISTER:
                return register_query.RegisterQuery(driver=driver)
            case Pages.USER_HOME:
                return home_query.UserHomeQuery(driver=driver)
            case Pages.ADMIN_HOME:
                return admin_home_query.AdminHomeQuery(driver=driver)
            case _:
                return login_query.LoginQuery(driver=driver)
