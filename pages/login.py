import logging

from common.base import BaseClass
from locators.login import LoginLocators

logger = logging.getLogger()


class LoginPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def login_button(self):
        return self.app.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    def login_button_click(self):
        self.login_button().click()

    def _username_input(self):
        return self.app.driver.find_element(*LoginLocators.USERNAME_INPUT)

    def _password_input(self):
        return self.app.driver.find_element(*LoginLocators.PASSWORD_INPUT)

    def auth(self, email: str, password: str):
        logger.info(
            f"Пытаемся залогиниться с помощью логина: {email} и пароля: {password}"
        )
        self.input_value(self._username_input(), email)
        self.input_value(self._password_input(), password)
        self.login_button_click()

    def auth_alert(self):
        return self.app.driver.find_element(*LoginLocators.ALERT)

    def auth_alert_get_text(self):
        return self.app.driver.find_element(*LoginLocators.ALERT).text
