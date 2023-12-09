# Первый Шаг: Откройте таинственный сайт с помощью Selenium, готовьтесь встретиться лицом к лицу с девятью рунными-стражами.
# Битва с Рекламой: Нажмите на любую кнопку, и как только это произойдет, перед вами появится назойливое рекламное окно. Ваша задача – быстро и решительно закрыть его, не давая ему нарушить ваш путь к секретам.
# Поиски Секретов: Как только реклама будет побеждена, обратите внимание на кнопку, которую вы только что освободили. На ней появятся подобные символы "01V5" – фрагмент древнего кода.
# Создание Ключа: Скопируйте символы и соберите из них длинный ключ в формате "YS93-R9R3-S019-PPI7-OS80-012C". Разделители "-" помогут вам организовать код и сделать его готовым к использованию.
# Порядок: Кликать можно в любом порядке, но собирать и "склеивать" его, необходимо в определённом порядке.

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/5/index.html')

    boxes = driver.find_elements(By.CLASS_NAME, 'box_button')
    result = []

    for box in boxes:
        box.click()
        time.sleep(3)
        ad = driver.find_element(By.ID, 'ad_window')
        driver.find_element(By.ID, 'close_ad').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(ad))
        time.sleep(3)
        result.append(box.text)

    print(*result, sep='-')
