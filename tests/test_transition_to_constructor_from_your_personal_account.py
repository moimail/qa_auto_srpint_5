
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Вход через лавную страницу
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
#Ожидание кнопки входа на главной странице
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

# Поиск кнопки входа
element = driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
element.click()


#Ожидание окна ввода данных
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))
#Ввод почты
element = driver.find_element(By.XPATH, './/input[@name="name"]')
element.send_keys("moimial@mail.ru")

#Ввод пароля
element = driver.find_element(By.XPATH, './/input[@name="Пароль"]')
element.send_keys("Qw123!")

#Нажатие на кнопку вход
element = driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
element.click()

#Переход в личный кабинет
element = driver.find_element(By.XPATH, './/header/nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]')
element.click()

#Ожидание открытия личного кабинет
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/nav/ul/li[1]/a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))

#Переход в конструктор из личного кабинета
element = driver.find_element(By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2"]')
element.click()

#Ожидание открытия конструктора
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/section[1]/h1[@class="text text_type_main-large mb-5 mt-10"]')))
driver.quit()