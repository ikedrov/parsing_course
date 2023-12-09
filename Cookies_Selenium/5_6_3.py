# Запуск: Откройте основной сайт с помощью Selenium. С этой точки начнётся ваша экспедиция в поисках "Бессмертного Печенюшка".
#
# Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.
#
# Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.
#
# Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/5/index.html')
    urls = [i for i in driver.find_elements(By.CLASS_NAME, 'urls')]
    expiry = []

    for u in urls:
        u.click()
        expiry.append(driver.get_cookie('foo2')['expiry'])
        driver.back()

    max_expiry = expiry.index(max(expiry)) + 1
    driver.get(f'https://parsinger.ru/methods/5/{max_expiry}.html')
    result = driver.find_element(By.ID, 'result').text

    print(result)



