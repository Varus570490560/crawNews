from time import sleep

import requests


def get_today_story():
    sleep(5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response = requests.get(url='https://www.ign.com', headers=headers)
    print(response)
    print(response.content)
