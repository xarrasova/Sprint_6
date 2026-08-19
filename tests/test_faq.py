import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FAQ_DATA


@allure.feature("Вопросы о важном")
class TestFAQ:

    @allure.title("Проверка ответов на вопросы")
    @allure.description("При клике на каждый вопрос открывается соответствующий текст")
    @pytest.mark.parametrize("question_index, expected_text", FAQ_DATA)
    def test_faq_answers(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open()

        answer_text = main_page.get_faq_answer_text(question_index)

        assert expected_text in answer_text, f"Ответ на вопрос {question_index + 1} не совпадает"