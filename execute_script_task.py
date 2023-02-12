from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x = browser.find_element(By.ID, "input_value").text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввести ответ в текстовое поле
    input_box = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_box.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
