# Вход в Лабиринт: Откройте указанный веб-сайт с помощью Selenium.
# Ключи к Сокровищам: Извлеките данные из каждого тега <p> на странице.
# Сложение Фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
# Отчет о Сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное значение вставьте в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.html')
    summ = 0
    nums = driver.find_elements(By.TAG_NAME, 'p')
    for i in nums:
        summ += int(i.text)

    print(summ)
