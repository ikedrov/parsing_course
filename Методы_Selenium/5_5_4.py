# Случайная Локация: Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из них будут чекбоксы. Главная загвоздка: чекбоксы и их состояние ("checked" или нет) определяются случайным образом.
#
# Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех, которые имеют рядом "checked" чекбоксы.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    result = []
    driver.get('https://parsinger.ru/selenium/5.5/3/1.html')
    fields = driver.find_elements(By.CLASS_NAME, 'parent')

    for field in fields:
        if field.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            result.append(int(field.find_element(By.TAG_NAME, 'textarea').text))

    print(sum(result))
