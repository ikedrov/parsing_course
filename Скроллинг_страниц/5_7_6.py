# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
# Техника скроллинга: Сайт содержит список из 100 элементов, которые появляются только при скроллинге. Стандартные элементы типа чекбоксов или другие элементы для "зацепления" тут отсутствуют.
#
# Навигация: Прокрутите страницу до самого низа, используя ActionChains.
#
# Сбор информации: Извлеките все числовые значения из появившихся элементов и сложите их.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')
    tags_list = []
    actions = ActionChains(driver)
    counter = 0
    flag = True
    driver.find_element(By.CLASS_NAME, 'scroll-container')
    while flag:
        tags = driver.find_elements(By.TAG_NAME, 'p')
        for i in tags:
            if i not in tags_list and i.text:
                actions.move_to_element(i)
                actions.perform()
                actions.reset_actions()
                counter += int(i.text)
                tags_list.append(i)
                if i.get_attribute('class') == 'last-of-list':
                    flag = False
    print(counter)