# Подготовка: Загрузите список сайтов, на которых скрыты коды.
# Открытие вкладок: Используя Selenium, откройте каждый сайт в отдельной вкладке.
# Поиск кодов: Пройдитесь по всем вкладкам и найдите чекбокс. Нажмите на него, чтобы получить код.
# Обработка данных: Для каждого полученного кода найдите его квадратный корень.
# Суммирование: Сложите все полученные корни.
# Финальное преобразование: Округлите конечную сумму до 9 знаков после запятой.

import time

from selenium.webdriver.common.by import By
from selenium import webdriver


sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as driver:
    result = 0
    for i in sites:
        driver.execute_script(f'window.open("{i}");')
        time.sleep(1)
    for x in range(1, len(driver.window_handles)):
        driver.switch_to.window(driver.window_handles[x])
        driver.find_element(By.CLASS_NAME, 'checkbox_class').click()
        result += int(driver.find_element(By.ID, 'result').text) ** 0.5
    print(round(result, 9))