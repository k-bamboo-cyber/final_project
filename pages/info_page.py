import logging

from common.base import BaseClass
from locators.info_page import InfoPageLocators

logger = logging.getLogger()


class InfoPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def first_name(self):
        return self.app.driver.find_element(*InfoPageLocators.FIRSTNAME_INPUT)

    def first_name_text(self):
        return self.first_name().text

    def last_name(self):
        return self.app.driver.find_element(*InfoPageLocators.LASTNAME_INPUT)

    def last_name_text(self):
        return self.last_name().text

    def zip_code(self):
        return self.app.driver.find_element(*InfoPageLocators.ZIP_CODE_INPUT)

    def zip_code_text(self):
        return self.zip_code().text

    def fill_info(self, firstname, lastname, zip_code):
        """Заполнение секции Информация"""
        logger.info(
            f"Пытаемся заполнить личные данные значениями "
            f"{firstname}, {lastname}, {zip_code}"
        )
        self.input_value(self.first_name(), firstname)
        self.input_value(self.last_name(), lastname)
        self.input_value(self.zip_code(), zip_code)

    def alert(self):
        return self.app.driver.find_element(*InfoPageLocators.ALERT)

    def check_alert(self):
        return self.alert().text

    def continue_button(self):
        return self.app.driver.find_element(*InfoPageLocators.CONTINUE_BUTTON)

    def continue_button_click(self):
        self.continue_button().click()
