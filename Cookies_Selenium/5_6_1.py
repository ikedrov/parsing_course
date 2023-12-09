# Вооружитесь браузером и пусть ваш код проникнет на сайт.
# Поиск секретных cookies: Найдите все скрытые secret_cookie_, которые могут содержать важную информацию
# Дешифровка и анализ: Суммируйте числовые значения всех secret_cookie_

from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    result = []
    for cookie in cookies:
        result.append(int(cookie['value']))
    print(sum(result))
