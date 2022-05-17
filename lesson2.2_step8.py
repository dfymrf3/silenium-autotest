import os
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os 
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    

    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kor")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("@mail")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
     
    



    button = browser.find_element_by_class_name("btn")
    button.click()
    
    


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

