# Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
# Поиск Ссылки: Используйте метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT для поиска ссылки с текстом 16243162441624.
# Клик по Ссылке: Нажмите на найденную ссылку.
# Получение Результата: Скопируйте текст, который появится в теге найденной страницы <p id="result"></p>.
# Фиксация: Запишите полученный результат в отдельную переменную или вставьте ответ в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/2/2.html')
    driver.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    result = driver.find_element(By.ID, 'result')
    print(result.text)
    time.sleep(5)
    