import unittest
import json
import traceback
import requests

url = 'http://cpright.xinhua-news.cn/api/match/image/getjson'
querystring = {
    'category': 'image',
    'offset': '0',
    'limit': '30',
    'sourceId': '0',
    'metaTitle': '',
    'metaId': '0',
    'classify': 'unclassify',
    'startTime': '',
    'endTime': '',
    'createStart': '',
    'createEnd': '',
    'sourceType': '',
    'isTracking': 'true',
    'metaGroup': '',
    'companyId': '0',
    'lastDays': '1',
    'author': ''
}
headers = {
    'cache-control': "no-cache",
    'postman-token': "e97a99b0-424b-b2a5-7602-22cd50223c15"
}
response = requests.request('POST', url, headers=headers, params=querystring)
results = json.loads(response.text)
print(results['total'])