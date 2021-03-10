import allure
import pytest

from common.constants import ButtonTexts


class TestLogout:
    @allure.story("Разлогин")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_logout(self, app, standard_login, clear_cart):
        """
        1. Открыть страницу магазина
        2. Авторизоваться
        3. Разлогиниться, открыв бургер
        4. Проверить, что есть список пользователей
        """
        app.main_page.try_logout()
        assert (
            app.login.get_users_list() == ButtonTexts.USERS_LIST
        ), "Ошибка при выходе из профиля"
