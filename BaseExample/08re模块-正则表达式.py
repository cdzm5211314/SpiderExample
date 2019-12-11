# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

import re

str1 = "I Study Python3.6 Everyday"

print("----- match() -----")
# match(): 从字符串起始位置进行匹配,如果起始位置匹配成功返回相应的匹配对象,如果不匹配返回None
m1 = re.match(r'I', str1)
m2 = re.match(r'.', str1)
m3 = re.match(r'\w', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'^I', str1)
print(m4.group())


print("----- search() -----")
# search(): 扫描整个字符串,如果匹配成功返回第一个匹配的位置的相应匹配对象,如果匹配不成功返回None
s1 = re.search(r'Study', str1)
s2 = re.search(r'S\w+', str1)
s3 = re.search(r'P\w+.\d', str1)
print(s3.group())



print("----- findall() -----")
# findall(): 查找全部:匹配整个字符串,如果匹配成功返回所有的匹配对象,如果匹配不成功返回None
fa1 = re.findall(r'y', str1)
print(fa1)

str2 = "<div><a herf='http://www.baidu.com'>阿里云aliyun</a></div>"

fa2 = re.findall(r"<a herf='http://www.baidu.com'>(.+)</a>", str2)
print(fa2)

fa3 = re.findall(r"herf='(.+)'", str2)
print(fa3)



print("----- sub() -----")
# sub(): 替换字符串
s1 = re.sub(r"<div>(.+)</div>", r"<span>\1</span>", str2)
print(s1)

