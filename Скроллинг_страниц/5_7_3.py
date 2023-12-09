# Откройте сайт с помощью Selenium.
# Найдите все четыре кнопки на странице.
# Определите значение value каждой кнопки. Это время, которое необходимо удерживать кнопку.
# Как только все кнопки станут зелёными, вы получите сообщение в alert. Скопируйте это сообщение.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/5/index.html')
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    actions = ActionChains(driver)
    for button in buttons:
        hold_time = float(button.text)
        actions.click_and_hold(button).pause(hold_time).release(button).perform()

    print(driver.switch_to.alert.text)

