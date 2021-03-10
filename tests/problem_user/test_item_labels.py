import allure
import pytest

from common.constants import ButtonTexts


class TestItemLabels:
    @allure.story("Просмотр страницы товара")
    @allure.severity("critical")
    @pytest.mark.xfail(reason="problem user")
    def test_item_parts(self, app, problem_login):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Проверить, что на стр товара
        совпадают с главной заголовок, описание, цена, фото
        """
        n = app.main_page.choose_item()
        name = app.main_page.item_name_text(n)
        price = app.main_page.item_price_text(n)
        desc = app.main_page.item_desc_text(n)
        img = app.main_page.item_img_text(n)
        app.main_page.open_item_card(n)
        assert (
            name == app.item_page.item_name_text()
        ), "Название товара отличается от названия на главной стр"
        assert (
            price == app.item_page.item_price_text()
        ), "Цена товара отличается от цены на главной странице"
        assert (
            desc == app.item_page.item_desc_text()
        ), "Описание товара не совпадает с описанием на главной странице"
        assert (
            img == app.item_page.item_img_text()
        ), "Картинка товара не совпадает с картинкой на главной странице"

    @pytest.mark.xfail(reason="problem user")
    def test_item_buttons(self, app, problem_login, clear_cart):
        """
        1. Авторизоваться
        2. Выбрать один из товаров
        3. Отрыть страницу товара
        4. Проверить, что на стр товара есть
         кнопка для добавления в корзину или удаления из корзины
        """
        n = app.main_page.choose_item()
        app.main_page.open_item_card(n)
        assert (
            app.item_page.add_to_cart_btn_text() == ButtonTexts.ADD_TO_CART_BUTTON
            or app.item_page.add_to_cart_btn_text() == ButtonTexts.REMOVE_BUTTON
        ), "Текст кнопки некорректен"
        assert (
            app.item_page.back_btn_text() == ButtonTexts.BACK_BUTTON
        ), "Текст кнопки для возврата на главную стр некорректен"
