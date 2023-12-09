# Стартовая Позиция: Запустите Selenium и откройте данный веб-сайт. Убедитесь, что ваша станция готова к операции.
#
# Сбор Урана: Пройдитесь по каждому кусочку урана на странице и кликните по нему. Это поможет нам вернуть его обратно на корабль.
#
# #Подсказка
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# Получение Секретного Кода: Как только в открытом космосе не останется ни одного кусочка урана, команда пришлёт вам в alert-окне секретный код.

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/1/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'button-container')
    for button in buttons:
        element = button.find_element(By.CLASS_NAME, 'clickMe')
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()

    print(driver.switch_to.alert.text)
