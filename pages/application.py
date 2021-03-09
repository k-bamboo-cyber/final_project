import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage
from pages.main_page import MainPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage
from common.logger import setup

logger = logging.getLogger()


class Application:
    def __init__(self, headless, url):
        setup("INFO")
        logger.setLevel("INFO")
        options: Options = Options()
        if headless:
            options.add_argument("--headless")
        self.url = url
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except ValueError:
            self.driver = webdriver.Chrome(r"C:\chromedriver.exe", options=options)
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self)
        self.main_page = MainPage(self)
        self.item_page = ItemPage(self)
        self.cart_page = CartPage(self)
        self.info_page = InfoPage(self)
        self.overview_page = OverviewPage(self)
        self.finish_page = FinishPage(self)

    def open_main_page(self):
        logger.info("Open main page")
        self.driver.get(self.url)

    def browser_close(self):
        self.driver.quit()
