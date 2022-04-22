from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure")
    value_x = x.get_attribute("valuex")

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(calc(value_x))

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
