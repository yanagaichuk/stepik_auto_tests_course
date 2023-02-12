from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.ID, "button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
