import pytest, time, math, ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ("https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1")


def time_result():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_should_see_result_link(browser, link):
    browser.get(link)
    button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                              ".ember-view.navbar__auth"
                                                                              ".navbar__auth_login")))
    button.click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys(ignore.login)
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys(ignore.password)
    button_auth = browser.find_element(By.CSS_SELECTOR, ".button_with-loader.sign-form__btn")
    button_auth.click()
    time.sleep(3)
    input_res = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    input_res.send_keys(time_result())
    button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    button.click()
    btn_again = browser.find_element(By.CSS_SELECTOR, ".again-btn")
    btn_again.click()
    output_result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert output_result.text == 'Correct!', output_result.text

    btn_ok = browser.find_element(By.CSS_SELECTOR, "#ember170 > button:nth-child(1)")
    btn_ok.click()
