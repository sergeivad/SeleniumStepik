from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.XPATH, '//input[@name = "firstname"]')
    firstName.send_keys('Sergei')

    lastName = browser.find_element(By.XPATH, '//input[@name = "lastname"]')
    lastName.send_keys('Elkin')

    email = browser.find_element(By.XPATH, '//input[@name = "email"]')
    email.send_keys('deazmont@yandex.ru')

    file = browser.find_element(By.ID, 'file')
    currDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currDir, 'temp.txt')
    file.send_keys(filePath)

    browser.find_element(By.XPATH, '//button[@type = "submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
