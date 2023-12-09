# Мир Цветов: Войдите на указанный сайт с помощью Selenium, где вас встретят яркие, цветные шарики, каждый из которых ждёт своей очереди, чтобы оказаться в своём уютном контейнере.
# Задача Сортировки: Ваша миссия - написать скрипт, который поможет каждому шарику найти его дом, соответствующий по цвету блок. Используйте свои знания и умения, чтобы аккуратно и внимательно перенести каждый шарик в его контейнер.

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/4/index.html')
    time.sleep(1)

    balls = driver.find_elements(By.CLASS_NAME, 'ball_color')
    baskets = driver.find_elements(By.CLASS_NAME, 'baskets_color')
    actions = ActionChains(driver)

    for ball in balls:
        color = ball.get_attribute('class').split()[1].split('_')[0]
        for basket in baskets:
            basket_color = basket.get_attribute('class').split()[1]
            if color == basket_color:
                actions.drag_and_drop(ball, basket).perform()

    print(driver.find_element(By.CLASS_NAME, 'message').text)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/selenium/5.10/4/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     time.sleep(1)
#     balls = driver.find_elements(By.CLASS_NAME, 'ball_color')
#     baskets = driver.find_elements(By.CLASS_NAME, 'basket_color')
#     actions = ActionChains(driver)
#
#     for ball in balls:
#         color_ball = ball.get_attribute('class').split()[1].split('_')[0]
#         for basket in baskets:
#             color_basket = basket.get_attribute('class').split()[1]
#             if color_ball == color_basket:
#                 actions.drag_and_drop(ball, basket).perform()
#
#     print(driver.find_element(By.CLASS_NAME, 'message').text)

