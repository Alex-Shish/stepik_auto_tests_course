from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time

def calc(x):
  return str(log(abs(12 * sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем нужную цену и кликаем кнопку
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    # вычисляем контрольное значение
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    # вставляем полученное значение в поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

