# Место преступления: Откройте указанный сайт с помощью Selenium.
#
# Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.
#
# Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить". При верном пин-коде вы получите секретный код.

from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')
    pin_codes = [i.text for i in driver.find_elements(By.TAG_NAME, 'span')]
    for code in pin_codes:
        driver.find_element(By.TAG_NAME, 'input').click()
        alert = driver.switch_to.alert
        alert.send_keys(code)
        alert.accept()
        result = driver.find_element(By.ID, 'result').text
        if result.isdigit():
            print(result)
            break
