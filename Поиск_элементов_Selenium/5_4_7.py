# Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
# Извлечение Ключей: Получите значения всех элементов выпадающего списка.
# Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
# Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
# Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as driver:
    result = 0
    driver.get('https://parsinger.ru/selenium/7/7.html')
    options = driver.find_elements(By.TAG_NAME, 'option')
    for option in options:
        result += int(option.text)

    driver.find_element(By.ID, 'input_result').send_keys(result)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    answer = driver.find_element(By.ID, 'result')
    print(answer.text)
    time.sleep(5)



