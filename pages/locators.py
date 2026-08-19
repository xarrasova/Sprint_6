# pages/locators.py
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer(index):
        return (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")


class OrderPageLocators:
    """Локаторы для страницы заказа"""
    
    # ----- Первая форма: "Для кого самокат" -----
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # ----- Вторая форма: "Про аренду" -----
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_DAYS = (By.XPATH, "//div[@class='Dropdown-menu']/div")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    
    # ----- Модальное окно подтверждения -----
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")