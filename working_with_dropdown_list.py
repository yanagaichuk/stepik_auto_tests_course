from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(a, b):
    return int(a) + int(b)

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    res = calc(num1, num2)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
