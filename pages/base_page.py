from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)
        return self

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    @allure.step("Найти элемент и ввести текст: {text}")
    def send_keys_to_element(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Найти элемент и получить его текст")
    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, main_window_handle):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        self.wait.until(lambda driver: driver.current_url != "about:blank")
        return self

    @allure.step("Принять куки")
    def accept_cookies(self, cookie_locator):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(cookie_locator))
            cookie_button.click()
        except:
            pass
        return self

    @allure.step("Дождаться появления элемента")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))