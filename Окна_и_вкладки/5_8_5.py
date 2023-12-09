# Инициализация: Запустите браузер через Selenium и загрузите страницу.
# Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) область страницы точно соответствовала 555x555 пикселям. Не забудьте учесть размеры рамок и панелей браузера при расчете!
# Анализ: Когда условие будет выполнено секретный ключ появится в id="result";


from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/1/')
    driver.set_window_size(555, 555+129)
    res = driver.find_element(By.ID, 'result').text

    print(res)