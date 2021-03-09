from common.constants import Users, ButtonTexts, Alerts

import pytest
import allure

from models.fake_data import UserData


class TestAuth:
    user = UserData.random()

    @allure.story("Авторизация")
    @allure.severity("blocker")
    @pytest.mark.parametrize(
        "email, password",
        (
            (Users.STANDARD_USERNAME, Users.PASSWORD),
            (Users.PROBLEM_USERNAME, Users.PASSWORD),
            (Users.PER_GLITCH_USERNAME, Users.PASSWORD),
        ),
    )
    def test_valid_auth(self, email, password, app):
        """
        1. Открыть страницу
        2. Ввести валидные значения в поля логина и пароля
        3. Нажать кнопку LOGIN
        4. Проверить, что в бургере есть кнопка Logout
        """
        app.open_main_page()
        app.login.auth(email, password)
        assert (
            app.main_page.logout_button_text() == ButtonTexts.LOGOUT_BUTTON_TEXT
        ), "Кнопка Logout не найдена"

    @pytest.mark.parametrize(
        "email, password, alert",
        (
            (Users.LOCKED_OUT_USERNAME, Users.PASSWORD, Alerts.LOCKED_OUT_ALERT),
            (user.login, user.password, Alerts.NON_EXIST_USER_ALERT),
            (Users.EMPTY_USERNAME, user.password, Alerts.EMPTY_MAIL_ALERT),
            (user.login, Users.EMPTY_PASSWORD, Alerts.EMPTY_PASSWORD_ALERT),
        ),
    )
    def test_invalid_auth(self, app, email, password, alert):
        """
        1. Открыть страницу
        2. Ввести невалидные данные
        3. Проверить содержимое алертов
        """
        app.open_main_page()
        app.login.auth(email, password)
        assert app.login.auth_alert_get_text() == alert, "Некорректные алерты"
