# Для этой задачи потребуется код с прошлого степа.
#
# Откройте сайт с помощью selenium;
# У вас есть 2 списка с размера окон size_x и size_y;
# Цель: определить размер окна, при котором,  в id="result" появляется число;
# Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
# ps. При написании кода, учитывайте размер рамок браузера.

from selenium.webdriver.common.by import By
from selenium import webdriver
from itertools import product

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/2/index.html')
    for x, y in product(window_size_x, window_size_y):
        driver.set_window_size(x, y + 129)
        result = driver.find_element(By.ID, 'result').text
        if result:
            print(driver.get_window_size())