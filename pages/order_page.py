from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='* Имя']"))
        ).send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(surname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)

        metro_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']")
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro)

        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select-search__select")))
        stations = self.driver.find_elements(By.XPATH, "//div[@class='select-search__select']//button")
        for station in stations:
            if station.text == metro:
                station.click()
                break

        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

    def fill_second_form(self, date, rental_days, color, comment):
        # Дата
        date_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='* Когда привезти самокат']"))
        )
        date_input.click()
        date_input.send_keys(date)
        self.driver.find_element(By.TAG_NAME, "body").click()

        # Срок аренды
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Dropdown-placeholder"))).click()
        days = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='Dropdown-menu']/div"))
        )
        for day in days:
            if day.text == rental_days:
                day.click()
                break

        # Цвет
        if color == "black":
            self.driver.find_element(By.ID, "black").click()
        elif color == "grey":
            self.driver.find_element(By.ID, "grey").click()

        # Комментарий
        self.driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']").send_keys(comment)

        # Кнопка "Заказать" - ИЩЕМ ПО КЛАССАМ (как на скриншоте)
        order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"))
        )
        order_button.click()

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"))
        ).text