# Исследование Территории: Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.
#
# Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
# Проверка и Контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.
#
# Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код нужно будет вставить в поле для ответа на степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/4/1.html')
    fields = driver.find_elements(By.CLASS_NAME, 'parent')

    for field in fields:
        num = field.find_element(By.XPATH, ".//textarea[@color='gray']").text
        field.find_element(By.XPATH, ".//textarea[@color='blue']").send_keys(num)
        field.find_element(By.XPATH, ".//textarea[@color='gray']").clear()
        field.find_element(By.TAG_NAME, 'button').click()

    driver.find_element(By.ID, 'checkAll').click()
    # res = driver.find_element(By.ID, 'congrats').text
    # print(res)
    time.sleep(5)
