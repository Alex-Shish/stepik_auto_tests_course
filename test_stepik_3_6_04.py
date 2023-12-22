import pytest, time, math, ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-view.navbar__auth" ".navbar__auth_login"))).click()
    browser.find_element(By.ID, "id_login_email").send_keys(ignore.login)
    browser.find_element(By.ID, "id_login_password").send_keys(ignore.password)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               ".button_with-loader.sign-form__btn"))).click()
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'again-btn'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))).click()
    except TimeoutException:
        pass
    finally:
        pass

    WebDriverWait(browser, 15).until_not(
        EC.element_attribute_to_include((By.CSS_SELECTOR, ".textarea"), 'disabled'))
    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(time_result())
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()
    corr_mess_str = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text
    try:
        assert "Correct!" in corr_mess_str
    except TimeoutException:
        with open("unusual.log", "a") as file:
            file.write(corr_mess_str)
        raise AssertionError('Обнаружен необычный ответ, смотрите в файле unusual.log')


if __name__ == "__main__":
    pytest.main()
