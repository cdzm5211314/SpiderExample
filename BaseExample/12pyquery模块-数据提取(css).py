# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

# 安装: pip install pyquery
# api: https://pythonhosted.org/pyquery/
# css选择器与JQuery

from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import requests


# 初始化方式:
# 1.字符串: (常用方式)
# doc = pq(str)
# 2.url:
# doc = pq(url="http://www.baidu.com")
# 3.文件:
# doc = pq(filename="dome.html")


# css选择器: 获取节点
# doc('#main #top')             即获取当前节点
# doc('#main #top').children()  即获取子节点(先获取父节点然后使用children()方法获取子节点)
# doc('#main #top').parent()    即获取父节点(先当前节点然后使用parent()方法获取父节点)
# doc('#main #top').siblings()  即获取兄弟节点(先当前节点然后使用siblings()方法获取兄弟节点)

# css选择器: 获取属性
# a = doc('#main #top')
# attr1 = a.attr('href')
# attr2 = a.attr.href

# css选择器: 获取内容
# div = doc('#main #top')
# text1 = div.html()
# text2 = div.text()


url = "https://www.xicidaili.com/nn/"

headers = {
    "User-Agent":UserAgent().chrome
}

response = requests.get(url, headers=headers)

doc = pq(response.text)
# print(doc)

# ips = doc('#ip_list tr').eq(1).find('td').eq(1).text()

trs = doc('#ip_list tr')
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    type = trs.eq(num).find('td').eq(5).text()
    print("{}://{}:{}".format(type.lower(), ip, port))


