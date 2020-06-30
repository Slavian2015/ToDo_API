import requests

url = 'http://127.0.0.1:8000/apis/v1/1/'
headers = {'Authorization': 'Token 7005bc3b312f94283f182d58e63358d90d4963e9'}
r = requests.get(url, headers=headers)
print("1",r.text)