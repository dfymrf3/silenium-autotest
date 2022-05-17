import os
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try: 
    
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Ваш код, который заполняет обязательные поля
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element_by_id("book")
    btn.click()
    browser.execute_script("window.scrollBy(0, 150);")
    input1 = browser.find_element_by_id("input_value")
    x = input1.text
    y = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    
    


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

