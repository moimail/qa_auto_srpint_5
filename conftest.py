import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    """ Открываем окно веб-драйвера """
    driver = webdriver.Chrome()

    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    driver.quit()