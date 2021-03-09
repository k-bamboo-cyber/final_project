import allure

from common.constants import ButtonTexts


class TestItemActions:
    @allure.story("Добавление товара в корзину")
    @allure.severity("blocker")
    def test_item_add_to_cart(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Проверить, что при нажатии на кнопку
        товар добавляется в корзину и появляется кнопка удаления
        """
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        first = app.item_page.check_cart_number()
        app.item_page.add_to_cart_btn_click()
        assert (
            app.item_page.check_cart_number() == first + 1
        ), "Ошибка при добавлении товара в корзину"
        assert (
            app.item_page.remove_btn_text() == ButtonTexts.REMOVE_BUTTON
        ), "Отсутствует кнопка удаления"

    def test_remove_item(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Добавить товар в корзину
        5. Проверить, что при удалении товар исчезает из корзины
        """
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.add_to_cart_btn_click()
        first = app.item_page.check_cart_number()
        app.item_page.remove_btn_click()
        assert (
            app.item_page.check_cart_number() == first - 1
        ), "Ошибка при удалении товара из корзины"

    def test_back_to_main(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Вернуться на главную стр
        """
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        app.item_page.back_btn_click()
        assert (
            app.item_page.app_logo() is not None
        ), "Ошибка при возврате на главную стр"
