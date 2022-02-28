import mitmproxy.http


def request(flow: mitmproxy.http.HTTPFlow):
    url_set = set()
    with open('./url_cache/url.txt', 'a+') as a:
        with open('./url_cache/url.txt', 'r') as r:
            while True:
                line = r.readline()
                if not line:
                    break
                else:
                    line = line[:len(line)-1]
                    url_set.add(line)
        if 'https://mollusk.apis.ign.com/graphql?operationName=VideoPlayerProps' in flow.request.url:
            print('url='+flow.request.url)
            if flow.request.url not in url_set:
                a.write(flow.request.url)
                a.write('\n')
                a.flush()


class Counter:
    def __init__(self):
        self.num = 0


addons = [
    Counter()
]
