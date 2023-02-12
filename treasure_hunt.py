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
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    chest = browser.find_element(By.ID, 'treasure')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = chest.get_attribute('valuex')

    # Посчитать математическую функцию от x
    y = calc(x)

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
