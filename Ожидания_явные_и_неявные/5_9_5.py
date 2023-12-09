# Загадочный Замок: Начните свою экспедицию, открыв сайт с помощью Selenium.
# Таинственные Блоки: Блоки появляются благодаря магии атрибута display. Ваш щит и меч в этом бою – метод EC.visibility_of(element) или EC.visibility_of_element_located(locator)
# Карта Ключей: С вами список ID ids_to_find. Эти ID – не просто случайные символы, это карта к древнему коду, вам необходимо дождаться появления и кликнуть по блокам именно с этими ID.
# Секретный Код: Если вы правильно активируете все нужные порталы, перед вами раскроется алерт с древним кодом. Этот код – залог вашего успеха в решении задачи.
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/3/index.html')

    for i in ids_to_find:
        box = driver.find_element(By.XPATH, f'//*[@id="{i}"]')
        WebDriverWait(driver, 60).until(EC.visibility_of(box)).click()

    try:
        alert = Alert(driver)
        time.sleep(3)
        print(alert.text)
        alert.accept()
    except NoAlertPresentException:
        pass