# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

# 安装: pip install requests

import requests
from fake_useragent import UserAgent

# 获取响应状态码: response.status_code
# 获取访问地址: response.url
# 获取响应头信息: response.headers
# 获取请求头信息: response.request.headers
# 获取cookie信息: response.cookies
# 获取网页编码: response.encoding
# 获取响应内容(字符串): response.text
# 获取响应内容(字节): response.content.decode(utf-8)
# 获取响应内容(json字符串): response.json()


###############################################################################################
# requests模块发送get请求

url = "https://www.baidu.com/"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

res = requests.get(url, headers)

info = res.content.decode()
# print(info)


###############################################################################################
# requests模块发送get请求并带参数
url = "https://www.baidu.com/s?"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

params = {
    "wd": "阿里云"
}

res = requests.get(url, headers=headers, params=params)

info = res.content.decode()
# print(info)


###############################################################################################
# requests模块发送post请求并带参数
url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191001048396"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

from_data = {
    'email': '1810376****',
    'password': 'ch******'
}

res = requests.post(url, headers=headers, data=from_data)

info = res.content.decode()
# print(info)


###############################################################################################
# requests模块使用proxy代理发送get请求
url = "http://httpbin.org/get"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

proxies = {
    "HTTP": "http://183.164.239.148:9999"
}

res = requests.get(url, headers=headers, proxies=proxies)

info = res.content.decode()
# print(info)


###############################################################################################
# requests模块忽略ssl证书发送get请求
url = "https://www.12306.cn/index/"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

# 禁用安全请求内容
# 1. 针对requests 2.5.0版本以下的,不包含2.5.0版本
# from urllib3.exceptions import InsecureRequestWarning
# requests.urllib3.disable_warnings(InsecureRequestWarning)
# 2. 针对requests 2.5.0版本以上的,且包含2.5.0版本
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

res = requests.get(url, headers=headers, verify=False)

info = res.content.decode()
print(info)


###############################################################################################
# requests模块发送psot请求并使用cookie信息
login_url = "http://www.sxt.cn/index/login/login"

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome,
}

form_data = {
    "user": "1810376****",
    "password": "123456",
}

# 登录操作
session = requests.Session()
# res = requests.post(login_url, headers=headers,data=form_data)
res = session.post(login_url, headers=headers, data=form_data)

# 登录后的操作
info_url = "http://www.sxt.cn/index/user.html"

res = session.get(info_url, headers=headers)

info = res.content.decode()
# print(info)


