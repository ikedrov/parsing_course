# Взлом Кодового Замка: Откройте веб-сайт с помощью Selenium.
# Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
# Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
# Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/4/4.html')
    checks = driver.find_elements(By.CLASS_NAME, 'check')
    for check in checks:
        check.click()
    driver.find_element(By.CLASS_NAME, 'btn').click()
    result = driver.find_element(By.ID, 'result')
    print(result.text)
    time.sleep(5)