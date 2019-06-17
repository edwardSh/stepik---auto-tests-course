from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome(executable_path="D:/chromedriver_win32_1/chromedriver.exe")
link = \
    "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



price = WebDriverWait(browser, 25).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
button = browser.find_element_by_css_selector("[id = 'book']")
button.click()

x_element = browser.find_element_by_css_selector("[id = 'input_value']")
x = x_element.text
print(x)

y = calc(x)
print(y)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

button = browser.find_element_by_css_selector("[type = 'submit']")
button.click()

