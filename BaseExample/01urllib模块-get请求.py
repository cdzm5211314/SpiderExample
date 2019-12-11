# -*- coding:utf-8 -*-
# @Desc : 百度贴吧
# @Author : Administrator

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent



def get_html(url):
    ua = UserAgent()
    headers = {
        "User-Agent":ua.chrome
    }
    req = Request(url, headers=headers)
    res = urlopen(req)
    return res.read().decode()


def save_html(filename, str_html):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str_html)


def run():
    # https://tieba.baidu.com/f?ie=utf-8&kw=阿里云&pn=100
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"

    content = input("你要下载的内容: ")
    num = input("你要下载的多少页: ")

    # 构建请求url
    for pn in range(int(num)):
        args = {
           "kw":content,
           "pn":pn * 50
        }
        url = base_url.format(urlencode(args))
        filename = "第" + str(pn+1) + "页.html"
        # print(url).

        print("正在下载" + filename)
        str_html = get_html(url)
        save_html(filename, str_html)
        print(filename + "下载完成")


if __name__ == '__main__':
    run()

