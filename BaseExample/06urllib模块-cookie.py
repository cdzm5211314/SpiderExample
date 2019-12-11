# -*- coding:utf-8 -*-
# @Desc : 人人网登陆后
# @Author : Administrator


from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

# url = "http://www.renren.com/893394172"
url = "https://www.sxt.cn/profile/course"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
    "Cookie":"UM_distinctid=16e732ddabeca-07fe8abb13b0c8-43450521-100200-16e732ddac01d4; user=a%3A2%3A%7Bs%3A2%3A%22id%22%3Bi%3A11122%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2218103763930%22%3B%7D; CNZZDATA1261969808=1246357314-1573888408-https%253A%252F%252Fwww.baidu.com%252F%7C1573960560"
}


# 携带登陆后的cookie进行访问
req = Request(url, headers=headers)

res = urlopen(req)

info = res.read().decode()
print(info)


