# Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
# Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
# Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
# Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.html')
    summ = []
    nums = driver.find_elements(By.CLASS_NAME, 'text')
    for i in nums:
        num = i.find_element(By.XPATH, './p[2]')
        summ.append(int(num.text))

    print(sum(summ))