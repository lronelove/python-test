import requests

def post_test():
    url = "http://localhost:3000/test"

    payload = "username=jack&password=jack&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "5c00397e-b7b3-4a01-bebe-0825d057855b"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.text

