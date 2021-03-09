import logging
import random
import time

from common.base import BaseClass
from locators.main_page import MainPageLocators

logger = logging.getLogger()


class MainPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def menu_button(self):
        return self.app.driver.find_element(*MainPageLocators.MENU_BUTTON)

    def menu_button_click(self):
        self.menu_button().click()

    def sort_button(self):
        return self.app.driver.find_element(*MainPageLocators.SORT_DROPDOWN)

    def sort_button_click(self):
        self.sort_button().click()

    def az_sort_button(self):
        return self.app.driver.find_element(*MainPageLocators.AZ_SORT_BUTTON)

    def az_sort_button_click(self):
        self.az_sort_button().click()

    def za_sort_button(self):
        return self.app.driver.find_element(*MainPageLocators.ZA_SORT_BUTTON)

    def za_sort_button_click(self):
        self.za_sort_button().click()

    def lh_sort_button(self):
        return self.app.driver.find_element(*MainPageLocators.L_TO_H_BUTTON)

    def lh_sort_button_click(self):
        self.lh_sort_button().click()

    def hl_sort_button(self):
        return self.app.driver.find_element(*MainPageLocators.H_TO_L_BUTTON)

    def hl_sort_button_click(self):
        self.hl_sort_button().click()

    def parsing_items(self) -> dict:
        """Парсинг неймов и цен товаров."""
        prices = self.app.driver.find_elements(*MainPageLocators.ITEM_PRICE)
        prices_new = []
        for p in prices:
            prices_new.append(p.text)
        names = self.app.driver.find_elements(*MainPageLocators.ITEM_NAME)
        names_new = []
        for n in names:
            names_new.append(n.text)
        items = dict(zip(names_new, prices_new))
        return items

    def check_az_sorting(self):
        """Проверка результатов сортировки по алфавиту(возр)."""
        self.sort_button_click()
        self.az_sort_button_click()
        names = list(self.parsing_items().keys())
        if sorted(names) == names:
            return True
        return False

    def check_za_sorting(self):
        """Проверка результатов сортировки по алфавиту(убыв)."""
        self.sort_button_click()
        self.za_sort_button_click()
        names = list(self.parsing_items().keys())
        if sorted(names, reverse=True) == names:
            return True
        return False

    def check_lh_sorting(self):
        """Проверка результатов сортировки возр-ю цены."""
        self.sort_button_click()
        self.lh_sort_button_click()
        prices = list(self.parsing_items().values())
        res = []
        for p in prices:
            p = float(p.replace("$", ""))
            res.append(p)
        if sorted(res) == res:
            return True
        return False

    def check_hl_sorting(self):
        """Проверка результатов сортировки убыв-ю цены"""
        self.sort_button_click()
        self.hl_sort_button_click()
        prices = list(self.parsing_items().values())
        res = []
        for p in prices:
            p = float(p.replace("$", ""))
            res.append(p)
        if sorted(res, reverse=True) == res:
            return True
        return False

    def logout_button(self, wait_time=5):
        logger.info("Пытаемся разлогиниться")
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(*MainPageLocators.LOGOUT_BUTTON)
            if len(element) > 0:
                return element[0]
            time.sleep(0.5)
        return 0

    def logout_button_click(self):
        """Если кнопка выхода найдена, нажимаем её и выходим из аккаунта"""
        if self.logout_button() != 0:
            self.logout_button().click()

    def logout_button_text(self):
        m = self.logout_button().text
        return m

    def try_logout(self):
        logger.info("Пытаемся разлогиниться")
        self.menu_button_click()
        self.logout_button_click()

    def twitter_button(self):
        return self.app.driver.find_element(
            *MainPageLocators.TWITTER_BUTTON
        ).find_element(*MainPageLocators.A)

    def twitter_button_href(self):
        return self.twitter_button().get_attribute("href")

    def facebook_button(self):
        return self.app.driver.find_element(
            *MainPageLocators.FACEBOOK_BUTTON
        ).find_element(*MainPageLocators.A)

    def facebook_button_href(self):
        return self.facebook_button().get_attribute("href")

    def linkedin_button(self):
        return self.app.driver.find_element(
            *MainPageLocators.LINKEDIN_BUTTON
        ).find_element(*MainPageLocators.A)

    def linkedin_button_href(self):
        return self.linkedin_button().get_attribute("href")

    def choose_item(self):
        items = self.app.driver.find_elements(*MainPageLocators.ITEM)
        res = random.randint(1, len(items))
        return res

    def item_name(self, n):
        names = self.app.driver.find_elements(*MainPageLocators.ITEM_NAME)
        return names[n - 1]

    def item_name_text(self, n):
        k = self.item_name(n).text
        return k

    def open_item_card(self, n):
        self.item_name(n).click()

    def item_price(self, n):
        prices = self.app.driver.find_elements(*MainPageLocators.ITEM_PRICE)
        return prices[n - 1]

    def item_price_text(self, n):
        k = self.item_price(n).text
        return k

    def item_desc(self, n):
        descriptions = self.app.driver.find_elements(*MainPageLocators.ITEM_DESC)
        return descriptions[n - 1]

    def item_desc_text(self, n):
        k = self.item_desc(n).text
        return k

    def item_img(self, n):
        images = self.app.driver.find_elements(*MainPageLocators.ITEM_IMG)
        return images[2 * n - 1]

    def item_img_text(self, n):
        k = self.item_img(n).get_attribute("src")
        return k

    def cart_icon(self):
        return self.app.driver.find_element(*MainPageLocators.CART_ICON)

    def cart_icon_click(self):
        self.cart_icon().click()
