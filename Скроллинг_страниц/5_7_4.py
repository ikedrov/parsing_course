# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
# Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span
# Вычисление: Соберите все эти числа и сложите их.

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    result = 0
    driver.get('https://parsinger.ru/scroll/2/index.html')
    divs = driver.find_elements(By.CLASS_NAME, 'item')
    for div in divs:
        checkbox = div.find_element(By.CLASS_NAME, 'checkbox_class')
        driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()
        try:
            result += int(div.find_element(By.TAG_NAME, 'span').text)
        except:
            pass
        
    print(result)

