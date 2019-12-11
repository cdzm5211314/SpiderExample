# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


from fake_useragent import UserAgent
import requests
from lxml import etree
from urllib import request


url = "http://www.farmer.com.cn/2019/12/06/99846244.html"

headers = {
    "User-Agent": UserAgent().chrome,
}

response = requests.get(url, headers=headers)

htmlElement = etree.HTML(response.content.decode("utf-8"))

title = htmlElement.xpath("//h1/text()")[0]
# print(type(title), title)

content_list = htmlElement.xpath("//div[@id='article_main']//p")
# content_list = ["".join(text.xpath(".//text()")) for text in content_list]
contents = []
for text in content_list:
    info = "".join(text.xpath(".//text()"))
    # print(type(info))
    contents.append(info + "\n")
    # contents.append("".join(text.xpath(".//text()")))

content = ''.join(contents)
# print(type(content), content)

# content = htmlElement.xpath("string(//div[@id='article_main']//p)")

img_urls = htmlElement.xpath("//div[@id='article_main']//p/img/@src")
# print(img_urls)

img_names = [ "图片" + str(i) for i in range(1, len(img_urls) + 1)]
# for name in img_names:
#     print(type(name), name)

# urlib库直接下载图片
for url, name in zip(img_urls, img_names):
    request.urlretrieve(url, name + ".jpg")

# 保存爬虫的文章内容
with open(title + ".txt", "w", encoding="utf-8") as ft:
    ft.write(content)


