# Стартовая Позиция: Используя Selenium, откройте заданный веб-сайт. Убедитесь, что ваша машина готова к операции.
#
# Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.
#
# Проверка: Нажмите на кнопку "Проверить" на странице.
#
# Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/2/1.html')
    fields = [i for i in driver.find_elements(By.CLASS_NAME, 'text-field')]
    for field in fields:
        if field.is_enabled():
            field.clear()
    driver.find_element(By.ID, 'checkButton').click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
