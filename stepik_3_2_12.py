"""
Для unittest существуют собственные дополнительные правила:
Тесты обязательно должны находиться в специальном тестовом классе.
Вместо assert должны использоваться специальные assertion методы.

Давайте теперь изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest.
Для этого нам понадобится выполнить следующие шаги:
1. Импортировать unittest в файл: import unittest
2. Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
3. Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве
   первого аргумента функции: def test_abs1(self):
   Изменить assert на self.assertEqual()
4. Заменить строку запуска программы на unittest.main()
"""

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
    def test_abs2(self):
        self.assertEqual(abs(-42), -42,"Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()
