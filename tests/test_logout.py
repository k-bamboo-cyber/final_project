import allure

from common.constants import ButtonTexts


class TestLogout:
    @allure.story("Разлогин")
    @allure.severity("critical")
    def test_logout(self, app, standard_login):
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
