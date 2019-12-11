# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import ssl

url = "https://www.12306.cn/index/"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome
}

req = Request(url, headers=headers)

# 忽略验证证书
context = ssl._create_unverified_context()

res = urlopen(req, context=context)

info = res.read().decode()
print(info)


