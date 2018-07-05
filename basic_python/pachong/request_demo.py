import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/', headers=headers)
try:
    print(res.text)
except ConnectionError:
    print('拒绝连接')
