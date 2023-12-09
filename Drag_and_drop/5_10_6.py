# Встреча с Цветными Блоками: Посетите указанный сайт и вы увидите множество цветных блоков, каждый из которых ждет своего момента, чтобы встретить свою пару.
# Танец Пар: Ваша задача - написать скрипт на Selenium, который поможет каждому блоку найти и соединиться со своей парой. Пара определяется по цвету блока, и именно цвет будет вашим проводником в этом танце.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/5.10/3/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(2)  # Даем странице время для загрузки

    draganddrops = driver.find_elements(By.CSS_SELECTOR, ".draganddrop.ui-draggable")
    draganddrop_ends = driver.find_elements(By.CSS_SELECTOR, ".draganddrop_end")

    for draganddrop in draganddrops:
        color = draganddrop.value_of_css_property("background-color")
        target = None
        for end in draganddrop_ends:
            border_color = end.value_of_css_property("border-top-color")
            if color == border_color:
                target = end
                break

        if target:
            ActionChains(driver).drag_and_drop(draganddrop, target).perform()
            time.sleep(0.5)  # Даем время для обработки действия

    time.sleep(2)  # Даем время для появления сообщения
    message = driver.find_element(By.ID, "message").text
    print("Сообщение:", message)

