# -*- coding:utf-8 -*-
# @Desc : 豆瓣网爬取电影
# @Author : Administrator


from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20"

ua = UserAgent()

num = 0
while True:
    headers = {
        "User-Agent": ua.chrome
    }
    url = base_url.format(num * 20)
    req = Request(url, headers=headers)

    res = urlopen(req)

    info = res.read().decode()
    print(type(info), info)

    # 判断是否还能获取内容,不能则退出循环
    if info == "[]" or info is None:
        break

    num += 1

