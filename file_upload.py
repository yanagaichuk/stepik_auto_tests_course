from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    first_name.send_keys('a')
    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    last_name.send_keys('A')
    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    email.send_keys('a@a.com')

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

