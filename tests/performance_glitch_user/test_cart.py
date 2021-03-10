import allure
import pytest


class TestItemActions:
    @allure.story("Добавление товара в корзину")
    @allure.severity("blocker")
    @pytest.mark.xfail(reason="glitch user")
    def test_card_remove(self, app, glitch_login, clear_cart):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Проверить, что при удалении товар исчезает из корзины
        """
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.add_to_cart_btn_click()
        app.item_page.back_btn_click()
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.add_to_cart_btn_click()
        app.main_page.cart_icon_click()
        first = app.item_page.check_cart_number()
        app.cart_page.remove_button_click()
        assert app.item_page.check_cart_number() == (
            first - 1
        ), "Ошибка при удалении товара "
