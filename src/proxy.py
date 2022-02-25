import mitmproxy.http
from mitmproxy import ctx


def request(flow: mitmproxy.http.HTTPFlow):
    if 'https://mollusk.apis.ign.com' in flow.request.url:
        print(flow.request.url)


class Counter:
    def __init__(self):
        self.num = 0


addons = [
    Counter()
]
