# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

import requests
from fake_useragent import UserAgent
from urllib.parse import quote  # url地址转码


url = "https://www.guazi.com/bj/buy/"

headers = {
    "User-Agent": UserAgent().chrome,
}

# response = requests.get(url, headers=headers)
# response.encoding = "utf-8"
# print(response.text)
# print(response.content.decode("utf-8"))


### Splash与Python结合使用
# 使用源代码: render.html
# splash_url = "http://192.168.59.130:8050/render.html?url={}&wait=1"  # wait=1 等待1秒加载
# response = requests.get(splash_url.format(url), headers=headers)
# print(response.content.decode("utf-8"))


# 使用PNG图片: render.png
# wait=1 等待1秒加载, width=1000 图片宽度, height=700 图片高度, render_all=1 长图截图
# splash_url = "http://192.168.59.130:8050/render.png?url={}&wait=1&render_all=1"
# response = requests.get(splash_url.format(url), headers=headers)
# with open("guazi.png","wb") as ft:
#     ft.write(response.content)


# 使用Lua脚本: execute
lua_script = """
function main(splash, args)
  splash:go('{}')
  splash:wait(1)
  return splash:html()
end
""".format(url)  # 拼接要访问的URL链接

# splash_url = "http://192.168.59.130:8050/execute?lua_source={}".format(quote(lua_script))  # lua_source拼接Lua脚本
splash_url = "http://192.168.59.130:8050/execute?lua_source={}".format(lua_script)  # lua_source拼接Lua脚本
response = requests.get(splash_url, headers=headers)  # 发送请求

print(response.content.decode("utf-8"))



