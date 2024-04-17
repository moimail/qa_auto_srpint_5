from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Регистрация

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

#Ожидание ссылки "Войти"
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/main/div/div/p/a[@class="Auth_link__1fOlj"]')))

#Переход по ссылке "Войти"
element = driver.find_element(By.XPATH, './/main/div/div/p/a[@class="Auth_link__1fOlj"]')
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
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')))
element = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
element.click()
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

driver.quit()