import allure


class TestSorting:
    @allure.story("Сортировка товаров")
    @allure.severity("minor")
    def test_az_sorting(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать сортировку в алфавитном порядке(по возрастанию)
        3. Проверить, что товары отсортированы
        """
        assert (
            app.main_page.check_az_sorting()
        ), "Ошибка при сортировке по алфавиту(a->z)"

    def test_za_sorting(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать сортировку в алфавитном порядке(по убыванию)
        3. Проверить, что товары отсортированы
        """
        assert (
            app.main_page.check_za_sorting()
        ), "Ошибка при сортировке по алфавиту(z->a)"

    def test_lh_sorting(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать сортировку по ценам(по возрастанию)
        3. Проверить, что товары отсортированы
        """
        assert (
            app.main_page.check_lh_sorting()
        ), "Ошибка при сортировке цены по возрастанию"

    def test_hl_sorting(self, app, standard_login):
        """
        1. Авторизоваться
        2. Выбрать сортировку по ценам(по убыванию)
        3. Проверить, что товары отсортированы
        """
        assert (
            app.main_page.check_hl_sorting()
        ), "Ошибка при сортировке цены по убыванию"

    def test_switch_sort(self, app, standard_login):
        """
        1. Авторизоваться
        2. Последовательно переключать сортировки
        3. Убедиться, что товары при переключении сортируются корректно
        """
        assert (
            app.main_page.check_az_sorting()
        ), "Ошибка при сортировке по алфавиту(a->z)"
        assert (
            app.main_page.check_za_sorting()
        ), "Ошибка при сортировке по алфавиту(z->a)"
        assert (
            app.main_page.check_lh_sorting()
        ), "Ошибка при сортировке цены по возрастанию"
        assert (
            app.main_page.check_hl_sorting()
        ), "Ошибка при сортировке цены по убыванию"
