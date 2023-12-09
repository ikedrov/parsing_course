# Инициализация: Используя Selenium, откройте заданный сайт.
# Анализ списков размеров: У вас есть два списка размеров – window_size_x и window_size_y.
# Тестирование: Примените каждое сочетание размеров из этих списков к окну вашего браузера.
# Поиск результата: После каждой установки размера проверяйте содержимое элемента с идентификатором id="result" на странице.
# Извлечение данных: Как только найдете уникальное сочетание, при котором на странице появляется число, скопируйте его и вставьте в поле для ответа.

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
            print(result)
            break