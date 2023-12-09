# Откройте Таинственную Страницу: Используя Selenium, откройте веб-страницу, где хранится первая подсказка.
#
# Решение Загадки: Найдите значение математического уравнения.
#
#
# Ключ к Выпадающему Списку: Откройте выпадающий список и выберите элемент с числом, которое у вас получилось на предыдущем этапе.
#
# Активация Механизма: Нажмите на кнопку на странице, если значение верное, вы получите код.
#
# Завершение Миссии: Скопируйте число, которое появится на странице после нажатия на кнопку, и вставьте его в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:

    driver.get('https://parsinger.ru/selenium/6/6.html')
    equation = driver.find_element(By.ID, 'text_box').text
    ev_eq = eval(equation)
    driver.find_element(By.XPATH, f'//option[text()={ev_eq}]').click()
    driver.find_element(By.CLASS_NAME, 'btn').click()
    answer = driver.find_element(By.ID, 'result')
    print(answer.text)
    time.sleep(5)
