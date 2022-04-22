from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//button[@type = "submit"]').click()

    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))

    browser.find_element(By.XPATH, '//button[@type = "submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
