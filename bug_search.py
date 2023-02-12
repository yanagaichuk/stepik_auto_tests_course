"""
У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте. Однако
разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная страница
доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.
Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с
ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который
создали разработчики. Это хорошо!
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    input3.send_keys("aaa@aa.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
