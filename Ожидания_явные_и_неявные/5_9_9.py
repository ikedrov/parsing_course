# Вход в Светящийся Мир: Откройте сайт с помощью Selenium и подготовьтесь к встрече с чек боксами и кнопками, которые готовы вас встретить в своем танце мерцания.
# Поиск Своей Пары: В этом танце каждая кнопка имеет свою пару - чек бокс. Ваша задача - следить за этими парами и ловить момент, когда чек бокс рядом с кнопкой перейдет в состояние "checked".
# Точное Время для Действия: Как только вы заметите, что чек бокс активировался, немедленно кликайте по соответствующей кнопке. Будьте внимательны и быстры, ведь светящиеся элементы не терпят медлительности.
# Поиски Секретного Кода: После успешного клика по каждой кнопку, извлеките секретный код, который откроется перед вами в теге <p id="result"></p> . Этот код - ключ к разгадке загадки и ваш билет к следующему этапу приключения.

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/7/index.html')

    containers = driver.find_elements(By.CLASS_NAME, 'container')
    for container in containers:
        check = container.find_element(By.CLASS_NAME, 'checkbox-container').find_element(By.TAG_NAME, 'input')

        WebDriverWait(driver, 30).until(EC.element_to_be_selected(check))
        container.find_element(By.TAG_NAME, 'button').click()

    print(driver.find_element(By.ID, 'result').text)
