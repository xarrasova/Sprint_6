import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Логотипы")
class TestLogo:
    
    @allure.title("Проверка перехода на главную страницу Самоката")
    @allure.description("Клик по логотипу Самоката должен открывать главную страницу")
    def test_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        # Кликаем по логотипу Самоката
        main_page.click_samokat_logo()
        
        # Проверяем, что мы на главной странице
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не перешли на главную страницу"
    
    @allure.title("Проверка перехода на Дзен")
    @allure.description("Клик по логотипу Яндекса должен открывать Дзен в новом окне")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        # Кликаем по логотипу Яндекса
        main_page.click_yandex_logo()
        
        # Проверяем, что открылся Дзен
        assert "dzen.ru" in driver.current_url, "Не перешли на Дзен"