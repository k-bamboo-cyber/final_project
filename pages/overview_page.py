import logging

from common.base import BaseClass
from locators.overview_page import OverviewPageLocators

logger = logging.getLogger()


class OverviewPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def finish_button(self):
        return self.app.driver.find_element(*OverviewPageLocators.FINISH_BUTTON)

    def finish_button_click(self):
        self.finish_button().click()
