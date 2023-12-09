# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
# Множественная навигация: На сайте есть 5 разных окон, в каждом из которых подгружается по 100 элементов при скроллинге.
#
# Техника скроллинга: Для каждого окна прокрутите страницу до самого низа. Здесь можно использовать ActionChains для эффективного скроллинга.
#
# Сбор информации: Из каждого окна извлеките все числовые значения и сложите их. Суммируйте данные из всех окон.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_3/')
    result = 0
    for i in range(1, 6):
        tags_list = []
        actions = ActionChains(driver)
        counter = 0
        flag = True
        container = driver.find_element(By.CLASS_NAME, f'scroll-container_{i}')
        while flag:
            spans = container.find_elements(By.TAG_NAME, 'span')
            for s in spans:
                if s not in tags_list and s.text:
                    actions.move_to_element(s)
                    actions.perform()
                    actions.reset_actions()
                    counter += int(s.text)
                    tags_list.append(s)
                    if s.get_attribute('class') == 'last-of-list':
                        flag = False
        result += counter
    print(result)






