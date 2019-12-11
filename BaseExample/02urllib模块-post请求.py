# -*- coding:utf-8 -*-
# @Desc : 人人网登陆
# @Author : Administrator


from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome
}

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191001048396"

from_data = {
    'email': '1810376****',
    'password': '****123456'
}

from_data = urlencode(from_data)

# post请求data参数是bytes类型数据
req = Request(url, data=from_data.encode(), headers=headers)

res = urlopen(req)

info = res.read().decode()
print(info)













