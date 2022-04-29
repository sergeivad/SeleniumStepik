import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def registration_form(link="http://suninjuly.github.io/registration1.html"):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
    first_name.send_keys("Ivan")

    second_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
    second_name.send_keys("Petrov")

    email = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
    email.send_keys("sample@mail.ru")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    time.sleep(5)
    browser.quit()

    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        welcome_text = registration_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Не найден текст после заполнения формы")

    def test_abs2(self):
        welcome_text = registration_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Не найден текст после заполнения формы")


if __name__ == "__main__":
    unittest.main()
