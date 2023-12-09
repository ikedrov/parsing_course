# Вход в Виртуальный Мир: Откройте указанный сайт с помощью Selenium, и погрузитесь в мир, где ваши действия определяют исход событий.
# Задача Перемещения: На сайте вас встретят два поля. В одном из них - красный блок, который ждет вашей помощи, чтобы пересечь границы и оказаться во втором поле. Используйте Selenium для написания скрипта, который аккуратно перетащит красный блок из первого поля во второе.
# Появление Токена: Как только блок достигнет своей цели, на сцене появится токен - символ вашего успеха и умения справляться с задачами. Ваша следующая миссия - взять этот токен и вставить его в поле для ответа, чтобы закрепить свою победу.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/1/index.html')

    start = driver.find_element(By.ID, 'draggable')
    finish = driver.find_element(By.ID, 'field2')

    actions = ActionChains(driver)
    actions.drag_and_drop(start, finish).perform()

    print(driver.find_element(By.ID, 'result').text)