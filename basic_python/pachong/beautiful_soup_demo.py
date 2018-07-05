import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

res = requests.get('https://www.17zixueba.com/',headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
soup = BeautifulSoup(res.text, 'lxml')
# title = soup.select('#pager > section:nth-of-type(5) > ul > li:nth-of-type(3) > a > div > p.skuDes')
titles = soup.select('#pager > section:nth-of-type(5) > ul > li > a > div > p.skuDes')
for title in titles:
    print(title.get_text())