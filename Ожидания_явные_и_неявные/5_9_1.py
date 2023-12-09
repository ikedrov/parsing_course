# Вход на сайт: Откройте загадочный сайт с помощью Selenium.
# Ожидание: На сайте есть кнопка, но она не активна сразу. Она "пробуждается" в случайный момент времени, в течение 1-3 секунд после загрузки.
# Быстрый рефлекс: После нажатия на эту кнопку, начните наблюдение за заголовком страницы (title). Он будет меняться, и вам нужно действовать стремительно!
# Момент правды: Когда заголовок страницы станет "345FDG3245SFD", быстро извлеките код из элемента с id="result".

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/3/index.html')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    WebDriverWait(driver, 20).until(EC.title_is('345FDG3245SFD'))
    print(driver.find_element(By.ID, 'result').text)