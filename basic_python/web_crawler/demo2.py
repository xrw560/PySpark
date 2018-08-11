from bs4 import BeautifulSoup
import requests

post_dict = {
    "btn": "%B5%C7%C2%BC",
    "handlekey": "login_frm1",
    "logins": 1,
    "password": '33',
    "Username": "22",
    "Verifycode": 8888
}

response = requests.post(
    url="http://www.yiqixue.com/User/CheckUserLogin.asp",
    data=post_dict
)

print(response.text)
cookie_dict = response.cookies.get_dict()
print(cookie_dict)
