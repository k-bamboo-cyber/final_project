import logging

from common.base import BaseClass
from locators.cart_page import CartPageLocators

logger = logging.getLogger()


class CartPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def remove_button(self):
        return self.app.driver.find_elements(*CartPageLocators.REMOVE_BUTTON)

    def remove_button_click(self):
        res = self.remove_button()[0]
        res.click()

    def remove_all(self):
        logger.info("Удаляем все товары из корзины")
        res = self.remove_button()
        for r in res:
            r.click()

    def checkout_button(self):
        return self.app.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)

    def checkout_button_click(self):
        self.checkout_button().click()

    def shopping_button(self):
        return self.app.driver.find_element(*CartPageLocators.SHOPPING_BUTTON)

    def shopping_button_click(self):
        self.shopping_button().click()
