from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def registration_form(link="http://suninjuly.github.io/registration1.html"):
    try:
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

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(5)
        browser.quit()