# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


# 需要安装: pip install lxml

# 节点关系:
# 父节点   parent
# 子节点   children
# 同胞节点  sibling
# 先辈节点  ancestor
# 后代节点  descendant


# 常用路径表达式:
# /             从根节点选取
# //            从匹配选择的当前节点选择文档中的节点,而不考虑它们的位置
# .             选择当前节点
# ..            选择当前节点的父节点
# @             选择属性
# text()        节点下的文本信息
# string(.)     把当前节点以及当前节点以下的所有文本都提取出来
# string(xpath)

# 通配符:
# *      匹配任何元素节点    xpath("div/*")     即获取div下的所有子节点
# @*     匹配任何属性节点    xpath("div[@*]")   即获取所有带属性的div节点
# node() 匹配任何类型节点


# 选取若干路径: |
# xpath("//div | //table")  即获取所有的div与table节点


# 谓语:
# xpath("/body/div[1]")             即获取body下第一个div节点
# xpath("/body/div[last()]")        即获取body下最后一个div节点
# xpath("/body/div[last()-1]")      即获取body下倒数第二个div节点
# xpath("/body/div[positon<3]")     即获取body下前两个个div节点
# xpath("/body/div[@class]")        即获取body下带有class属性的div节点
# xpath("/body/div[@class='main']") 即获取body下class属性为main的div节点
# xpath("/body/div[price>35.00]")   即获取body下price元素大于35的div节点


from lxml import etree
from fake_useragent import UserAgent
import requests

url = "https://www.qidian.com/finish?chanId=21"

headers = {
    "User-Agent":UserAgent().chrome
}

response = requests.get(url, headers=headers)

htmlEtree = etree.HTML(response.text)

# lis = htmlEtree.xpath("//div[@class='book-img-text']/ul/li")
# for li in lis:
#     names = htmlEtree.xpath("./div[@class='book-mid-info']/h4/a/text()")
#     authors = htmlEtree.xpath("./div[@class='book-mid-info']/p[1]/a[1]/text()")

names = htmlEtree.xpath("//div[@class='book-mid-info']/h4/a/text()")
authors = htmlEtree.xpath("//div[@class='book-mid-info']/p[1]/a[1]/text()")

# print(zip(names, authors))
for name, author in zip(names, authors):
    print(name + " ---> " + author)
    print(type(name), type(author))  # lxml.etree._ElementUnicodeResult


