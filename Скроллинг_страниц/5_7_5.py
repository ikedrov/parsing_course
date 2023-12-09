# Инициализация: Используя Selenium, откройте заданный веб-сайт.
#
# Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
#
# Сбор данных: Кликайте или скролльте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. Используйте Keys.DOWN или методы ActionChains(driver).
#
# Агрегация: Извлеките все числовые значения из этих элементов и сложите их.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_1/')
    span_list = []
    actions = ActionChains(driver)
    counter = 0
    flag = True
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    while flag:
        spans = driver.find_elements(By.TAG_NAME, 'span')
        for span in spans:
            if span not in span_list and span.text:
                actions.move_to_element(span.find_element(By.TAG_NAME, 'input'))
                actions.click()
                actions.perform()
                actions.reset_actions()
                counter += int(span.text)
                span_list.append(span)
                if span.get_attribute('class') == 'last-of-list':
                    flag = False
    print(counter)