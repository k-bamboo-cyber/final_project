import time
import logging

from common.base import BaseClass
from locators.item_page import ItemPageLocators

logger = logging.getLogger()


class ItemPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def item_name(self):
        return self.app.driver.find_element(*ItemPageLocators.ITEM_NAME)

    def item_name_text(self):
        return self.item_name().text

    def item_price(self):
        return self.app.driver.find_element(*ItemPageLocators.ITEM_PRICE)

    def item_price_text(self):
        return self.item_price().text

    def item_desc(self):
        return self.app.driver.find_element(*ItemPageLocators.ITEM_DESC)

    def item_desc_text(self):
        return self.item_desc().text

    def item_img(self):
        return self.app.driver.find_element(*ItemPageLocators.ITEM_IMG)

    def item_img_text(self):
        return self.item_img().get_attribute("src")

    def add_to_cart_btn(self):
        return self.app.driver.find_element(*ItemPageLocators.ADD_TO_CART_BTN)

    def add_to_cart_btn_click(self):
        return self.add_to_cart_btn().click()

    def add_to_cart_btn_text(self):
        return self.add_to_cart_btn().text

    def back_btn(self):
        return self.app.driver.find_element(*ItemPageLocators.BACK_BTN)

    def back_btn_text(self):
        return self.back_btn().text

    def back_btn_click(self):
        return self.back_btn().click()
        time.sleep(0.2)

    def cart_number(self):
        n = self.app.driver.find_elements(*ItemPageLocators.CART_NUMBER)
        time.sleep(0.3)
        return n

    def check_cart_number(self):
        if len(self.cart_number()) == 0:
            return 0
        else:
            return int(self.cart_number()[0].text)

    def remove_btn(self):
        return self.app.driver.find_element(*ItemPageLocators.REMOVE_BUTTON)

    def remove_btn_text(self):
        return self.remove_btn().text

    def remove_btn_click(self):
        return self.remove_btn().click()

    def app_logo(self):
        return self.app.driver.find_element(*ItemPageLocators.APP_LOGO)
