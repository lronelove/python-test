import requests


def get_ajax(url, params, payload):
    payload = payload or "" # 放在body里面的数据，采用pwd=jack&id=1的格式传递
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7c8163b6-bbbb-414f-96de-262c6d7eb0ac"
    }
    params = params or {} # 采用{ 'jack': 'jack' }格式传参
    response = requests.request("GET", url, data=payload, headers=headers, params=params)

    return response.text
