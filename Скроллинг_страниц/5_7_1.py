# Идентификация Элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# # Пример поиска элемента по ID
# browser.find_element(By.ID, 'btn')
# Получение Фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный элемент оказался в видимой области.
# # Пример получения фокуса элемента
# element = browser.find_element(By.CLASS_NAME, 'btn')
# browser.execute_script("return arguments[0].scrollIntoView(true);", element)
# Клик по Элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
# Проверка Результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату(в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
# Суммирование:  Суммируйте все полученные числа.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    result = 0
    driver.get('https://parsinger.ru/scroll/4/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'visibility')
    for button in buttons:
        element = button.find_element(By.CLASS_NAME, 'btn')
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        button.click()
        result += int(driver.find_element(By.ID, 'result').text)

    print(result)

