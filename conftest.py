import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия браузера Firefox"""
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    yield driver
    
    driver.quit()