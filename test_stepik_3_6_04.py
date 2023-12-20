import pytest
import time
from math import *
from ignore import login, password
from selenium import webdriver
from selenium.webdriver.common.by import By

links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]
#  Correct!
#  Correct!
#  Correct!
#  The owls
#  are not
#  Correct!
#  Correct!
#  what they seem! 0v0

#  The owls are not what they seem! OvO

for i in range(len(links)):
    def test_should_see_result_link():
        try:
            browser = webdriver.Chrome()
            browser.get(links[i])
            time.sleep(3)
            button = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login")
            button.click()
            input1 = browser.find_element(By.ID, "id_login_email")
            input1.send_keys(login)
            input2 = browser.find_element(By.ID, "id_login_password")
            input2.send_keys(password)
            button_auth = browser.find_element(By.CSS_SELECTOR, ".button_with-loader.sign-form__btn")
            button_auth.click()
            time.sleep(3)
            input_link1 = browser.find_element(By.CSS_SELECTOR, ".textarea")
            input_link1.send_keys(str(log(int(time.time()))))
            btn = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
            btn.click()
            btn2 = browser.find_element(By.CSS_SELECTOR, ".again-btn")
            btn2.click()
            output_result = browser.find_element(By.CSS_SELECTOR, ".ember-application")
            assert output_result.text == "Correct!", ''
            btn_ok = browser.find_element(By.CSS_SELECTOR, "#ember170 > button:nth-child(1)")
            btn_ok.click()
        finally:
            time.sleep(3)
            browser.quit()
