from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import randint

#Личный кабинет
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
# Личный кабинет
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
element.click()

#Ожидание окна ввода данных
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))

#Переход по гиипер ссылке "Зарегистрироваться"
element = driver.find_element(By.XPATH, './/div/div/p[1]/a[@class="Auth_link__1fOlj"]')
element.click()

#Ожидание окна ввода данных
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))

#Ввод имени
element = driver.find_element(By.XPATH, './/input[@name="name"]')
element.send_keys("Иван")

#Ввод почты
element = driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]')
element.send_keys(f"ivan{randint(1,100000)}@ya.ru")

#Ввод не корректного пароля
element = driver.find_element(By.XPATH, './/fieldset[3]/div/div/input')
element.send_keys(f"{randint(10000,99999)}")

#Нажатие на кнопку регстрации
element = driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
element.click()

#ожидание уведомления о не корректном пароле
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/fieldset[3]/div/p[@class="input__error text_type_main-default"]')))

#Ввод корректного пароля
element = driver.find_element(By.XPATH, './/fieldset[3]/div/div/input')
element.send_keys(f"{randint(100000,999999)}")

#Нажатие на кнопку регстрации
element = driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
element.click()

#Ожидание возможности входа
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')))
driver.quit()


