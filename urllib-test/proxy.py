from urllib import request, parse

data = {
    'username': 'lronelove',
    'password': 'w657828543'
}
proxy = request.ProxyHandler({
    'http': '192.168.191.1:7001'
})
url = 'http://192.168.191.1:7001/api/v1/login'
opener = request.build_opener(proxy)
request.install_opener(opener)
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url, data).read()
page = page.decode('utf-8')
print(page)