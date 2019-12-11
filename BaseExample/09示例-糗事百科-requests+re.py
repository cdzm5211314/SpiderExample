# -*- coding:utf-8 -*-
# @Desc : 糗事百科
# @Author : Administrator

import requests
from fake_useragent import UserAgent
import re


url = "http://www.lovehhy.net/Joke/Detail/QSBK/2"

headers = {
    "User-Agent":UserAgent().chrome
}

res = requests.get(url, headers=headers)

info = res.text
# print(info)

context = re.findall(r'<div id="endtext">(.+)</div>', info)

print(context)



