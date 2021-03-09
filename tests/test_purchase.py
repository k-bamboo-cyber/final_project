import allure
import pytest

from common.constants import Pictures, Alerts
from models.fake_data import UserData


class TestPurchase:
    user = UserData.random()
    user2 = UserData.random()

    @allure.story("Совершение покупки")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "firstname,lastname,zip_code",
        (
            (user.first_name, user.last_name, user.zip_code),
            (user2.first_name, user2.last_name, user2.zip_code),
        ),
    )
    def test_fast_purchase(self, app, standard_login, firstname, lastname, zip_code):
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.add_to_cart_btn_click()
        app.main_page.cart_icon_click()
        app.cart_page.checkout_button_click()
        app.info_page.fill_info(firstname, lastname, zip_code)
        app.info_page.continue_button_click()
        app.overview_page.finish_button_click()
        assert (
            app.finish_page.complete_img_source() == Pictures.COMPLETE_IMG
        ), "Ошибка при оформлении покупки"

    @pytest.mark.parametrize(
        "firstname, lastname, zip_code, alert",
        (
            ("", user.last_name, user.zip_code, Alerts.EMPTY_FIRSTAME_ALERT),
            (user.first_name, "", user.zip_code, Alerts.EMPTY_LASTAME_ALERT),
            (user.first_name, user.last_name, "", Alerts.EMPTY_ZIPCODE_ALERT),
        ),
    )
    def test_empty_info_fields(
        self, app, standard_login, firstname, lastname, zip_code, alert
    ):
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.add_to_cart_btn_click()
        app.main_page.cart_icon_click()
        app.cart_page.checkout_button_click()
        app.info_page.fill_info(firstname, lastname, zip_code)
        app.info_page.continue_button_click()
        assert app.info_page.check_alert() == alert, "Неверное сообщение алерта"
