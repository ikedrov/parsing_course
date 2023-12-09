# Открытие Мира: Используйте Selenium для того, чтобы открыть на сайт.
# Миссия Броска: В вашем распоряжении 8 кусочков и 8 цветных грядок. Каждая грядка обладает своей уникальной чертой - расстоянием, на которое необходимо бросить кусочек, чтобы он оказался в своей грядке. Ваша задача - написать скрипт, который с точностью и вниманием к деталям осуществит эти броски.

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(1)
    bed = {bed.get_attribute("id")[-3:]: int(bed.find_element(By.TAG_NAME, 'p').text[-5:-2])
           for bed in browser.find_elements(By.CLASS_NAME, 'range')}
    for piece in browser.find_elements(By.CLASS_NAME, 'piece'):
        ActionChains(browser).drag_and_drop_by_offset(
            piece, bed[piece.get_attribute("id")[-3:]], 0).perform()
    print(browser.find_element(By.ID, 'message').text)