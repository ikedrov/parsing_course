# Начало Путешествия: Войдите на указанный сайт с помощью Selenium, где четыре пронумерованных блока ужe ждут своего героя - красного квадрата.
# Миссия Перемещения: Ваша задача - написать скрипт, который возьмёт на себя роль проводника и поможет красному квадрату посетить каждый из этих блоков, перетаскивая его поочерёдно в каждый из них.
# Токен Победы: Как только красный квадрат посетит все блоки, на сцене появится токен - символ вашего успеха и завершения миссии. Этот токен необходимо будет вставить в поле для ответа, чтобы закрепить ваш успех и завершить задание.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/2/index.html')

    box = driver.find_element(By.ID, 'draggable')
    targets = driver.find_elements(By.CLASS_NAME, 'box')
    actions = ActionChains(driver)

    for target in targets:
        actions.drag_and_drop(box, target).perform()

    print(driver.find_element(By.ID, 'message').text)


