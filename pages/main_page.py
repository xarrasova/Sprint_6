from .base_page import BasePage
from .locators import MainPageLocators
from data.urls import Urls
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_page(Urls.MAIN_PAGE)
        self.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        return self

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.click_element(MainPageLocators.ORDER_TOP_BUTTON)
        return self

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_bottom(self):
        self.click_element(MainPageLocators.ORDER_BOTTOM_BUTTON)
        return self

    @allure.step("Получить текст ответа на вопрос FAQ #{index}")
    def get_faq_answer_text(self, index):
        question = self.wait_for_clickable(MainPageLocators.faq_question(index))
        question.click()
        answer = self.wait_for_element(MainPageLocators.faq_answer(index))
        return answer.text

    @allure.step("Клик по логотипу Самоката")
    def click_samokat_logo(self):
        self.click_element(MainPageLocators.SAMOKAT_LOGO)
        return self

    @allure.step("Клик по логотипу Яндекса и переход на новое окно")
    def click_yandex_logo(self):
        main_window = self.driver.current_window_handle
        self.click_element(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(main_window)
        return self