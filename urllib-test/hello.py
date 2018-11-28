from urllib import request
url = 'http://192.168.191.1:7001/api/v1/home/nav'

response = request.urlopen(url)
page = response.read()
page = page.decode('utf-8')
print(page)