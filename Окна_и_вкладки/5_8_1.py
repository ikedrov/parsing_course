# Запуск: Откройте указанный веб-сайт с использованием Selenium.
#
# Исследование: На странице размещено 100 кнопок. Отправьтесь в путешествие, кликая по каждой из них, чтобы понять, какая из них прячет желаемый код.
#
# Обнаружение: При активации правильной кнопки, секретный код появится в теге: <p id="result">Code</p>.

from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.TAG_NAME, 'input')
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        alert.accept()
        result = browser.find_element(By.TAG_NAME, 'p').text
        if result:
            print(result)
            break




