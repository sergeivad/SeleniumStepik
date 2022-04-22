from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text

    sum_n = int(number1) + int(number2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))

    select.select_by_value(str(sum_n))

    browser.execute_script("alert('Robots at work');")

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
