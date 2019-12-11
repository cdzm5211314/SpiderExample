# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

from urllib.request import Request, urlopen, ProxyHandler, build_opener
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
# url = "https://www.baidu.com/"

ua = UserAgent()
headers = { "User-Agent": ua.chrome }

req = Request(url, headers=headers)

# proxy = ProxyHandler({"HTTP":"username:password@ip:port"})
# proxy = ProxyHandler({"HTTP":"ip:port"})
proxy = ProxyHandler({"HTTP":"114.239.255.87:9999"})
opener = build_opener(proxy)

# res = opener.open(url)
res = opener.open(req)

info = res.read().decode()
print(info)


