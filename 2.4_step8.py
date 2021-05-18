from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))


button_book = browser.find_element_by_css_selector('button#book')
button_book.click()

button2 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

first_number = browser.find_element_by_id('input_value')
get_fir_nmb = first_number.text
p = calc(get_fir_nmb) #посчитали сумму
element_2 = browser.find_element_by_id('answer')
element_2.send_keys(p)

button2.click()
browser.switch