# Запустите ваш кибер-копатель и отправьтесь на заданный сайт.
#
# Особая задача сбора: Соберите только те "печеньки", значения которых имеют чётные числа после символа "_". Например, если cookie имеет имя "session_12", число "12" является чётным, и это именно то, что вам нужно.
#
# Анализ и суммирование: Суммируйте числовые значения этих особых "печенек". Это сумма будет вашим ключом.

from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    result = []
    for cookie in cookies:
        if int(cookie['name'].split('_')[-1]) % 2 == 0:
            result.append(int(cookie['value']))

    print(sum(result))
