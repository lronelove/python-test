import requests

url = "http://localhost:3000/home"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "7c8163b6-bbbb-414f-96de-262c6d7eb0ac"
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)