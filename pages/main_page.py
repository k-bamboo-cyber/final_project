import logging
from selenium.webdriver import ActionChains

from common.base import BaseClass
from locators.main_page import MainPageLocators

logger = logging.getLogger()


class MainPage(BaseClass):
    def __init__(self, app):
        self.app = app

    # def menu_button(self, wait_time=5):
    #     logger.info("Открываем сайдбар")
    #     timestamp = time.time() + wait_time
    #     while time.time() < timestamp:
    #         element = self.app.driver.find_elements(*MainPageLocators.LOGOUT_BUTTON)
    #         if len(element) > 0:
    #             return element[0]
    #         time.sleep(0.5)
    #     return 0
    #
    # def menu_button_click(self):
    #     """Если кнопка меню найдена, нажимаем её """
    #     if self.menu_button() != 0:
    #         self.menu_button().click()
    def menu_button(self):
        return self.app.driver.find_element(*MainPageLocators.MENU_BUTTON)

    def menu_button_click(self):
        self.menu_button().click()

    def logout_button(self):
        return self.app.driver.find_element(*MainPageLocators.LOGOUT_BUTTON)

    def logout_button_click(self):
        self.logout_button().click()

    def logout_button_text(self):
        self.logout_button().text

    def check_logout(self):
        logger.info("Проверяем, что присутствует кнопка разлогина")
        self.menu_button_click()
        self.logout_button_click()

    def try_logout(self):
        logger.info("Пытаемся разлогиниться")
        """
        1. Нажимаем кнопку ню в бургере
        2. В бургере нажимаем Logout
        3. Запускаем цепочку действий наведения мыши
        по этим элементам с кликом по Logout
        """
        menu = self.menu_button()
        logout = self.logout_button()
        ActionChains(self.app.driver).move_to_element(menu).move_to_element(
            logout
        ).click().perform()
