import os.path
import threading

import requests

import visit
import get_soup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
}


class GetTodayStory(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        visit.get_today_story()


class RunBrowser(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        urls = run_browser()
        visit_page(urls)


def run_browser():
    soup = get_soup.get_soup('https://www.ign.com', use_chrome=True)
    urls = visit.find_a(soup=soup)
    res = list()
    for url in urls:
        if url['href'].startswith('/news/') or url['href'].startswith('/wikis/') or url['href'].startswith(
                '/videos/') or url['href'].startswith('/articles/'):
            res.append(url['href'])
    return res


def visit_page(urls):
    base_url = ''
    for url in urls:
        soup = get_soup.get_soup(base_url + url, False)
        title = soup.find(name='title')
        if not os.path.isdir('./output/' + title.string):
            os.mkdir('./output/' + title.string)
        with open('./output/' + title.string + '/' + title.string + '.txt', 'wb') as writer:
            ps = soup.findAll(name='p')
            update = soup.find(name='div', attrs='jsx-2034901901 article-modified-date')
            if update is not None:
                writer.write(update.text.encode())
                writer.write('\n'.encode())
            for p in ps:
                print(p)
                writer.write(p.text.encode())
                writer.write('\n'.encode())
                writer.flush()
        imgs = soup.findAll(name='img')
        i = 0
        for img in imgs:
            if i == 0:
                i=i+1
                continue
            i=i+1
            src = img['src']
            index = src.find('?')
            src = src[:index]
            img_response = requests.get(url=src, headers=headers)
            with open('./output/' + title.string + '/' + str(i) + '.jpg', 'wb') as w:
                w.write(img_response.content)
                print(src)
