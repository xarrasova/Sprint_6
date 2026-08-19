import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного флоу заказа с разными данными")
    @pytest.mark.parametrize("order_data", [
        {
            "name": "Анна",
            "surname": "Харрасова",
            "address": "ул. Ленина, 1",
            "metro": "Сокольники",
            "phone": "89276542724",
            "date": "20.08.2026",
            "rental_days": "сутки",
            "color": "black",
            "comment": "Прошу позвонить за час",
            "button": "top"  # ← добавил кнопку в данные
        },
        {
            "name": "Анита",
            "surname": "Харрасова",
            "address": "пр. Мира, 15",
            "metro": "Комсомольская",
            "phone": "89161112233",
            "date": "21.08.2026",
            "rental_days": "двое суток",
            "color": "grey",
            "comment": "Без звонка",
            "button": "bottom"  # ← добавил кнопку в данные
        }
    ])
    def test_positive_order(self, driver, order_data):
        """Тест позитивного сценария заказа с разными данными"""
        
        main_page = MainPage(driver)
        main_page.open()
        
        # Кликаем по кнопке в зависимости от данных
        if order_data["button"] == "top":
            main_page.click_order_top()
        else:
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