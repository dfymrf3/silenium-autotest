from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("input_value")
    x = num1.text
    y = calc(x)

        
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    
    
    browser.execute_script("window.scrollBy(0, 150);")
    
    
    input3 = browser.find_element_by_id("robotsRule")
    
    input3.click()
    button = browser.find_element_by_class_name("btn")
    button.click()
    
    


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
