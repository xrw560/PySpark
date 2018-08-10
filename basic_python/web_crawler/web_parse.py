from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://www.autohome.com.cn/news/')
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, features="html.parser")
target = soup.find(id='auto-channel-lazyload-article')

li_list = target.find_all("li")
for li in li_list:
    a = li.find("a")
    if a:
        print(a.attrs.get('href'))
        txt = a.find("h3").text
        print(txt)
        img = a.find("img")
        img_url = img.attrs.get("src")
        print(img_url[2:])

        img_response = requests.get(url="https://"+img_url[2:])
        import uuid

        file_name = str(uuid.uuid4())+".jpg"
        with open(file_name, 'wb') as f:
            f.write(img_response.content)



