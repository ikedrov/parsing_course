# Открытие Мира: Используйте Selenium для того, чтобы ступить на порог виртуального пространства, где синий квадрат ожидает своего часа, чтобы начать своё путешествие.
# Синий Путник и Красные Ориентиры: На вашем пути встретятся красные точки, которые будут служить ориентирами и проверочными пунктами. Ваша задача - написать скрипт, который возьмёт на себя роль проводника, и аккуратно и последовательно проведёт синий квадрат через все красные точки, следуя по оси X(слева направо).
# Появление Токена: После того как последняя красная точка будет покорена, на экране появится токен - символ вашего успеха и точности в выполнении задачи.
# Завершение Миссии: Вставьте полученный токен в поле для ответа, тем самым завершив своё путешествие и подтвердив свои навыки владения Selenium.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/3/index.html')

    actions = ActionChains(driver)
    block = driver.find_element(By.ID, 'block1')
    actions.click_and_hold(block)

    for _ in range(6):
        actions.move_by_offset(50, 0)

    actions.perform()

    print(driver.find_element(By.ID, 'message').text)

