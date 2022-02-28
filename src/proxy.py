import mitmproxy.http


def request(flow: mitmproxy.http.HTTPFlow):
    with open('./url_cache/url.txt', 'wb') as w:
        if 'https://mollusk.apis.ign.com/' in flow.request.url:
            print(flow.request.url)
            w.write(flow.request.url.encode())
            w.write('\n'.encode())
            w.flush()


class Counter:
    def __init__(self):
        self.num = 0


addons = [
    Counter()
]
