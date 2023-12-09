# Перейдите на сайт
# Скачайте видео с сайта  при помощи requests
# Определите его размер вручную
# Напишите размер файла в поле для ответа. Написать нужно только цифру в мегабайтах.


import requests
import os

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'

response = requests.get(url=url, stream=True)

with open('file.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)

file_size = os.path.getsize('file.mp4')
print(file_size / 1048576)
