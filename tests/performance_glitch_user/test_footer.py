import allure
import pytest

from common.constants import Links


class TestFooter:
    @allure.story("Соцсети")
    @allure.severity("minor")
    @pytest.mark.xfail(reason="glitch user")
    def test_twitter_link(self, app, glitch_login):
        """
        1. Авторизоваться
        2. Проверить, что у иконки твиттера нужная ссылка
        """
        assert (
            app.main_page.twitter_button_href() == Links.TWITTER_LINK
        ), "Неправильная ссылка на твиттер"

    @pytest.mark.xfail(reason="glitch user")
    def test_facebook_link(self, app, glitch_login):
        """
        1. Авторизоваться
        2. Проверить, что у иконки фейсбука нужная ссылка
        """
        assert (
            app.main_page.facebook_button_href() == Links.FACEBOOK_LINK
        ), "Неправильная ссылка на facebook"

    @pytest.mark.xfail(reason="glitch user")
    def test_linkedin_link(self, app, glitch_login):
        """
        1. Авторизоваться
        2. Проверить, что у иконки linkedin нужная ссылка
        """
        assert (
            app.main_page.linkedin_button_href() == Links.LINKEDIN_LINK
        ), "Неправильная ссылка на linkedin"
