# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

# 安装: pip install bs4 或 pip install beautifulsoup4
# 如果bs4使用lxml解析,需要安装: pip install lxml


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
    <p class="title" id="test"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/chen" class="chen" id="chen">dong</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
</body>
"""


# 创建BeautifulSoup解析对象
bs = BeautifulSoup(html_doc, "lxml")


### beautifulsoup4的基本使用: find_all()提取数据 ---> 标签选择器查找
print("----- finad_all() -----")
print(bs.find_all('a'))                                     # 获取所有的a标签
print(bs.find_all('a', limit=2)[1])                         # 获取第二个a标签,limit表示最多获取2个元素
print(bs.find_all(id="test"))                               # 获取id属性值为test的标签
print(bs.find_all('a', class_="sister"))                    # 获取所有class="sister"的a标签,因为class在Python是关键字,所以使用class_
print(bs.find_all('a', attrs={"class":"sister"}))           # 获取所有class="sister"的a标签
print(bs.find_all('a', attrs={"id":"chen","class":"chen"})) # 获取id="chen",class="chen"的a标签
# 获取所有a标签的href属性
alist = bs.find_all('a')
for a in alist:
    # 1. 通过下标操作方式
    # href = a['href']
    # print(href)
    # 2. 通过attrs属性方式
    href = a.attrs['href']
    # print(href)

# 获取所有a标签的文本信息
alist = bs.find_all('a')
# for a in alist:
#     print(a.string)       # stripped_strings 获取非空白字符
#     print(a.get_text())



### beautifulsoup4的基本使用: select()提取数据 ---> css选择器查找
print("----- select() -----")
print(bs.select("a"))                                   # 通过标签名查找
print(bs.select(".sister"))                             # 通过类名: class="sister"查找
print(bs.select("#chen"))                               # 通过ID名: id="chen"查找
print(bs.select("a#chen"))                              # 组合查找: 标签名与类名,ID名组合查找
print(bs.select("head > title"))                        # 直接子标签查找
print(bs.select('a[href="http://example.com/chen"]'))   # 通过属性查找
print(bs.select("title")[0].get_text())                 # 获取标签的文本内容



