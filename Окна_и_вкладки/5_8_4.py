# Погружение в кибермир: Используя Selenium, перейдите на указанный сайт.
#
# Поиск зеркальных комнат: На сайте вы обнаружите 9 iframe. В каждом из них скрыта кнопка.
#
# Сбор информации: Нажмите на кнопку в каждом iframe, чтобы получить число. Но помните, с вероятностью 1/9 это число окажется тем самым ключом к сейфу.
#
# Открытие тайны: Вставьте полученное число в поле для проверки. Если удача на вашей стороне, то это число откроет перед вами секретный код в alert.

import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')
    for i in range(1, 10):
        time.sleep(2)  # Задержка перед переключением на iframe

        # Переход в iframe
        iframe = driver.find_element(By.ID, f'iframe{i}')
        driver.switch_to.frame(iframe)

        # Нажатие на кнопку
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Нажми меня')]")
        button.click()

        # Получение числа
        time.sleep(1)  # Задержка перед чтением числа
        number = driver.find_element(By.ID, 'numberDisplay')
        number_value = number.text

        # Возврат к основному содержимому
        driver.switch_to.default_content()

        # Ввод числа в поле и нажатие кнопки
        input_field = driver.find_element(By.ID, 'guessInput')
        input_field.clear()
        input_field.send_keys(number_value)

        check_btn = driver.find_element(By.ID, 'checkBtn')
        check_btn.click()

        try:
            # Получение текста из alert
            time.sleep(1)  # Задержка перед проверкой наличия alert
            alert = Alert(driver)
            print(alert.text)
            alert.accept()
            break
        except NoAlertPresentException:
            # Если alert не появляется, продолжаем со следующим iframe
            continue

