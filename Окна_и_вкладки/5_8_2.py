# Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту, где спрятаны улики.
#
# Внимательное расследование: На сайте находится 100 кнопок. Каждая из них при нажатии активирует всплывающее alert окно с пин-кодом.
#
# Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды. Ваша задача — ввести пин-код и проверить его. Если пин-код верный, вы получите секретный код.

from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/2/index.html')
    for button in driver.find_elements(By.TAG_NAME, 'input'):
        button.click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        driver.find_element(By.ID, 'input').send_keys(alert_text)
        driver.find_element(By.ID, 'check').click()
        result = driver.find_element(By.ID, 'result').text
        if result.isdigit():
            print(result)
            break

