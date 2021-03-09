import logging

from common.base import BaseClass
from locators.overview_page import OverviewPageLocators

logger = logging.getLogger()


class FinishPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def complete_img(self):
        return self.app.driver.find_element(*OverviewPageLocators.COMPLETE_IMG)

    def complete_img_source(self):
        return self.complete_img().get_attribute("src")
