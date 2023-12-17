"""
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё.
Ловить исключения не надо (во всяком случае, здесь)!
Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного
исключения.
Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestSelectors(unittest.TestCase):
    def test_input1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        self.input3.send_keys("ivan@smolensk.ru")
        self.button = self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        self.button.click()
        self.welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_text, 'Congratulations! You have successfully registered!', 'Ok!')
        self.browser.quit()
    def test_input2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        self.input3.send_keys("ivan@smolensk.ru")
        self.button = self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        self.button.click()
        self.welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_text, 'Congratulations! You have successfully registered!', 'Ok!')
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()