from urllib import request, parse

def get_page(url):
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'username': 'lronelove',
        'password': 'w657828543'
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers, data=data)

    try:
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
    except error.HTTPError as e:
        print(e.code())
        print(e.read().decode('utf-8'))
    return page

url = 'http://192.168.191.1:7001/api/v1/login'
print(get_page(url))
