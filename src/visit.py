from time import sleep

import requests
from bs4 import BeautifulSoup


def analysis_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content)
    print(soup.prettify())
    title = soup.find(name='title')
    with open('./essay/' + title.string + '.txt', 'wb') as writer:
        ps = soup.findAll(name='p')
        update = soup.find(name='div', attrs='jsx-2034901901 article-modified-date')
        writer.write(update.text.encode())
        writer.write('\n'.encode())
        for p in ps:
            print(p)
            writer.write(p.text.encode())
            writer.write('\n'.encode())
            writer.flush()


def get_today_story():
    sleep(5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response = requests.get(url='https://www.ign.com', headers=headers)
    print(response)
    soup = BeautifulSoup(response.content, 'lxml')
    articles = soup.findAll(name='article')
    for article in articles:
        print(article)
        for i, child in enumerate(article.descendants):
            if i == 0:
                analysis_article('https://www.ign.com' + child['href'])
