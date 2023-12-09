# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
# Бесконечный Скроллинг: На сайте есть блок с бесконечной подгрузкой чекбоксов. Всего 100 контейнеров и в каждом контейнере 10 чек боксов.
#
# Чётный Выбор: Устанавливайте чекбоксы только с чётным значением атрибута value.
# Алерт-Кнопка: После установки всех чекбоксов во всех контейнерах кнопка alert с классом alert_button. Нажмите на неё, чтобы вызвать сообщение alert , в alert и будет ключ к решению задачи.

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
    child_cont = browser.find_element(By.CSS_SELECTOR, 'div.child_container')
    while True:
        ActionChains(browser).scroll_to_element(child_cont).perform()
        elements = child_cont.find_elements(By.TAG_NAME, 'input')
        for checkbox in elements:
            if not int(checkbox.get_attribute("value")) % 2:
                checkbox.click()
        try:
            # поиск следующего элемента для скроллинга к нему на следующей итерации
            child_cont = child_cont.find_element(By.XPATH, 'following-sibling::div[@class="child_container"]')
        except:
            break # Когда элементы кончатся, выходим из цикла
    alert_button = browser.find_element(By.CSS_SELECTOR, ".alert_button")
    ActionChains(browser).scroll_to_element(alert_button).perform()
    alert_button.click()
    print(browser.switch_to.alert.text)