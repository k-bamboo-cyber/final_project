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
        self.remove_button()[0].click()

    def checkout_button(self):
        return self.app.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)

    def checkout_button_click(self):
        self.checkout_button().click()
