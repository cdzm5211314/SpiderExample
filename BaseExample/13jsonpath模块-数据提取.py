# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

import json

str = '{"name":"盗梦空间"}'
print(str, type(str))

# Json字符串转换为Python类型数据
p_str = json.loads(str)
print(p_str, type(p_str))

# 把文件中Json字符串读取出来
# r_str = json.load(open("movie.txt", encoding="utf-8"))
# print(r_str, type(r_str))


# Python类型数据转换为Json字符串
j_str = json.dumps(p_str, ensure_ascii=False)
print(j_str, type(j_str))

# Python类型数据写入到文件
j_str = json.dump(p_str, open("movie.txt", "w", encoding="utf-8"), ensure_ascii=False)


# 安装: pip install jsonpath

# xpath与jsonpath语法对比
# /     $       根节点
# .     @       当前节点
# /     .or[]   取子节点
# //    ..      在任意位置获取符合条件的节点
# *     *       匹配所有元素节点

from fake_useragent import UserAgent
from jsonpath import jsonpath
import requests

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {
    "User-Agent":UserAgent().chrome
}

response = requests.get(url, headers=headers)

# 需要把请求的Json字符串转换为Python类型数据
# names = jsonpath(json.loads(response.text), "$..name")
names = jsonpath(response.json(), "$..name")
codes = jsonpath(response.json(), "$..code")

for name,code in zip(names, codes):
    print(name + " ---> " + code)



