# -*- coding:utf-8 -*
import requests

def test():
    url = 'http://localhost:3000/'
    headers = {
        'content-type': 'application/json'
    }
    r = requests.get(url=url, headers=headers)

    return r.text

if __name__ == '__main__':
    print(1)
    print(test())