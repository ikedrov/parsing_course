# Врата в Неизведанное: Ваше путешествие начнется с открытия сайта с помощью Selenium. На этом сайте вас ждет кнопка.
# Танец Элементов: После нажатия на эту кнопку, страница начнет игру с вами — на экране появится множество элементов с различными классами.
# Испытание Откровения: Среди этого множества элементов вашей задачей будет отыскать тот единственный, который мерцает классом "BMH21YY". Но не пытайтесь обмануть судьбу, делая это вручную — ваша цель — применить метод presence_of_element_located(locator) и дождаться момента его появления.
# Секретные Глифы: Как только этот таинственный элемент обнаружен, извлеките его содержимое и внесите в поле для ответа.

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    locator = (By.CLASS_NAME, 'BMH21YY')
    result = WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
    print(result.text)