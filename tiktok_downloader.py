# https://www.tiktok.com/@codex_kg/video/7327987700139691271
# https://www.tiktok.com/@codex_kg/video/7327987700139691271?is_from_webapp=1&sender_device=pc&web_id=7289042945105217029

import requests, os

input_url = input('URL: ')
# print(input_url)
current_id = input_url.split('/')[5].split('?')[0]
print(current_id)
video_api = requests.get(f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id=7327987700139691271{current_id}').json()
print(video_api)
video_url = video_api.get('aweme_list')[0].get('video').get('play_addr')
print(video_url)
if video_url:
    print('Начинаю скачивать видео......')
    try:
        os.mkdir('video')
    except:
        print('Папка создана video')
    try:
        with open(f'video/{current_id}.mp4', 'wb') as video_file:
            video_file.write(requests.get(video_url).content)
            print("Видео успешно скачан папку video")
    except:
        print("Произошла ошибка")