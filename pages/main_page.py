from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators


class MainPage:
    """Главная страница Яндекс.Самокат"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def open(self):
        """Открыть главную страницу"""
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        self.accept_cookies()
        return self
    
    def accept_cookies(self):
        """Принять куки"""
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            )
            cookie_button.click()
        except:
            pass
    
    def click_order_top(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_TOP_BUTTON)
        ).click()
    
    def click_order_bottom(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BOTTOM_BUTTON)
        ).click()
    
    def get_faq_answer_text(self, index):
        """Получить текст ответа на вопрос по индексу (0-7)"""
        question = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.faq_question(index))
        )
        question.click()
        
        answer = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.faq_answer(index))
        )
        return answer.text
    
    def click_samokat_logo(self):
        """Клик по логотипу Самоката"""
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.SAMOKAT_LOGO)
        ).click()
    
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса и переход на новое окно"""
        main_window = self.driver.current_window_handle
        
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        logo.click()
        
        # Ждем появления нового окна
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        
        # Переключаемся на новое окно
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        
        # Ждем загрузки страницы
        self.wait.until(lambda driver: driver.current_url != "about:blank")