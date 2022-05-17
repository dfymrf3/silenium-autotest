from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    x = num1.text
    y = num2.text
    sum = str(int(x)+int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    
    button = browser.find_element_by_class_name("btn")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
