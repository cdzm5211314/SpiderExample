# -*- coding:utf-8 -*-
# @Desc : 使用requests发送请求,bs4-lxml解析响应数据,css(select)提取数据
# @Author : Administrator


from fake_useragent import UserAgent
import requests
from random import randint
import time
import re


## 发送请求并返回响应内容
def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome,
    }

    # 发送请求
    time.sleep(randint(3, 5))  # 避免请求频繁,适当的让程序睡眠几秒
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        # 返回响应内容
        return response.text
        # return response.content.decode("utf-8")
    else:
        return  None

## 解析每页电影的详情页url地址并返回
def parse_movie_url(html):

    # 使用lxml解析响应的文档信息
    # htmlElement = etree.HTML(html)

    # 使用xpath表达式提取 电影的 详情页的 url地址
    # //dl[@class="movie-list"]//dd/div[@class='movie-item']/a/@href
    # movie_urls = htmlElement.xpath("//div[@class='channel-detail movie-item-title']/a/@href")

    # 构建完整的电影详情url地址并返回
    # return ["https://maoyan.com{}".format(url) for url in movie_urls]

    ##########################################################################################

    # 使用bs4解析响应的文档信息
    # bs = BeautifulSoup(html, 'lxml')
    # 获取所有的a标签
    # 注: 如果标签的class属性值有多个 用.号连接
    # all_a = bs.select("div.channel-detail.movie-item-title > a")
    # movie_urls = []
    # for a in all_a:
        # movie_urls.append(a.attrs['href'])

    # 构建完整的电影详情url地址并返回
    # return ["https://maoyan.com{}".format(url) for url in movie_urls]

    ##########################################################################################

    # 使用re正则解析提取数据
    movie_urls = re.findall(r'<a href="(/films/\d+)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">.*</a>', html)

    # 构建完整的电影详情url地址并返回
    return ["https://maoyan.com{}".format(url) for url in movie_urls]

## 解析电影的详情页并提取所需数据
def parse_movie_detail(html):

    # 使用lxml解析响应的文档信息
    # htmlElement = etree.HTML(html)

    # 使用xpath表达式提取所需数据
    # movie_name = htmlElement.xpath("//h3[@class='name']/text()")[0]
    # print(type(movie_name))
    # movie_type = htmlElement.xpath("//div[@class='movie-brief-container']//li[1]/text()")[0]
    # movie_actor = htmlElement.xpath(
    #     '//div[@class="celebrity-container"]//ul/li[@class="celebrity actor"]//a[@class="name"]/text()')
    # movie_actor = [actor.strip() for actor in movie_actor]
    # print(movie_name, movie_type, movie_actor)

    ##########################################################################################

    # 使用bs4解析响应的文档信息
    # bs = BeautifulSoup(html, 'lxml')

    # 使用css选择器提取所需数据
    # movie_name = bs.select("div.movie-brief-container > h3")[0].text
    # movie_type = bs.select("div.movie-brief-container > ul > li:nth-child(1)")[0].text

    ##########################################################################################

    # 使用re正则解析提取数据
    movie_name = re.findall(r'<h3 class="name">(.*?)</h3>', html)[0]
    movie_type = re.findall(r'<li class="ellipsis">(.*?)</li>', html)[0]

    # 返回提取到的所需数据
    return {
        "movie_name": movie_name,
        "movie_type": movie_type,
    }


## 爬虫的逻辑处理
def main():

    url = "https://maoyan.com/films?offset=0"
    # 发送请求 - url页面起始页
    html = get_html(url)

    # 解析响应内容,返回电影详情页的url地址
    movie_urls = parse_movie_url(html)
    print(movie_urls)

    # 发送请求 - 电影详情页
    for url in movie_urls:
        movie_html = get_html(url)
        movie_dict = parse_movie_detail(movie_html)
        print(movie_dict)

    # 构造请求的url
    # base_url = "https://maoyan.com/films?offset={}"
    # for i in range(0, 90, 30):  # i变量控制页码 0 30 60 90
    #     html = get_html(url.format(str(i)))


if __name__ == '__main__':

    main()
