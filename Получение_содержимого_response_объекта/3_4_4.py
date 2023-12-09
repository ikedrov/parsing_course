# Напишите код, который скачает все 160 картинок с указанного сайта на ваш локальный компьютер.
#
# После скачивания, просмотрите картинки вручную и найдите на одной из них секретный код.

import requests

for i in range(1, 161):
    response = requests.get(f'https://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f'/Users/ivankedrov/parsing_stepik/3_4_4/image{i}.png', 'wb') as image:
        image.write(response.content)


