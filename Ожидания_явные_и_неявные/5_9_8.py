# Вход в Мир Таинства: Используйте Selenium для открытия указанного сайта и подготовьтесь к встрече с чек боксом, обладающим свойствами непредсказуемости.
# Погоня за Мгновением: Чек бокс, который вы встретите, обладает уникальной способностью внезапно появляться и исчезать. Он не любит, когда его ловят на месте, и потому ваша задача - быть настолько внимательным и быстрым, чтобы ухватить его в момент активации.
# Методы Ожидания: Вооружитесь методами ожидания Selenium, ибо только они помогут вам в этой неравной битве со временем и неопределенностью. Дождитесь момента, когда чек бокс активируется, и в тот же миг нажмите на кнопку "Проверить".

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/6/index.html')

    checkbox = driver.find_element(By.ID, 'myCheckbox')
    WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox))
    driver.find_element(By.TAG_NAME, 'button').click()
    print(driver.find_element(By.ID, 'result').text)