from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

        # Метро
        metro_input = self.wait_for_clickable(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro)

        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.METRO_SELECT))
        stations = self.find_elements((By.XPATH, "//div[@class='select-search__select']//button"))
        for station in stations:
            if station.text == metro:
                station.click()
                break

        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, rental_days, color, comment):
        # Дата
        date_input = self.wait_for_clickable(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.send_keys(date)
        self.click_body()  # ← вынесено в BasePage

        # Срок аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        days = self.find_elements(OrderPageLocators.RENTAL_DAYS)
        for day in days:
            if day.text == rental_days:
                day.click()
                break

        # Цвет
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

        # Комментарий
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

        # Кнопка "Заказать"
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_element_text(OrderPageLocators.SUCCESS_MESSAGE)