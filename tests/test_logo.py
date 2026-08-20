import allure
from pages.main_page import MainPage
from data.urls import Urls


@allure.feature("Логотипы")
class TestLogo:

    @allure.title("Проверка перехода на главную страницу Самоката")
    @allure.description("Клик по логотипу Самоката должен открывать главную страницу")
    def test_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_samokat_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE, "Не перешли на главную страницу"

    @allure.title("Проверка перехода на Дзен")
    @allure.description("Клик по логотипу Яндекса должен открывать Дзен в новом окне")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()

        assert Urls.DZEN_PAGE in main_page.get_current_url(), "Не перешли на Дзен"