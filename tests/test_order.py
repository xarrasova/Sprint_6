import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката (верхняя кнопка)")
    @allure.description("Проверка полного флоу заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_positive_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_top()

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, "Заказ не был оформлен"

    @allure.title("Позитивный сценарий заказа самоката (нижняя кнопка)")
    @allure.description("Проверка полного флоу заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_positive_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_bottom()

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, "Заказ не был оформлен"