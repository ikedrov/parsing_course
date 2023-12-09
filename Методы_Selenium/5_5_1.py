# Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта.
#
# Охота на Сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том, что оно появляется очень редко. Вам придется обновлять страницу множество раз, пока не увидите это число.
#
# Клад в Руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа на вашем курсе.

from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as driver:

    driver.get('https://parsinger.ru/methods/1/index.html')
    while True:
        result = driver.find_element(By.ID, 'result').text
        driver.refresh()
        if result.isdigit():
            print(result)
            break
