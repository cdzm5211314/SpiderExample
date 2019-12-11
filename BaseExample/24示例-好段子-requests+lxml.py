# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


from fake_useragent import UserAgent
import requests
from lxml import etree


# url管理器
class URLManager(object):

    def __init__(self):
        self.new_url = []  # 未爬取的url列表
        self.old_url = []  # 已爬取的url列表

    # 获取一个url
    def get_new_url(self):

        # pop()移除列表中的最后一个元素,并返回该元素的值
        url = self.new_url.pop()  # 即从列表中取出一个元素并移除
        self.old_url.append(url)  # 即添加一个已经爬取的url添加到列表

        return url

    # 增加一个url
    def add_new_url(self, url):

        # 判断添加进来的url是否存在,且不为空
        if url not in self.new_url and url and url not in self.old_url:
            self.new_url.append(url)

    # 增加多个url
    def add_new_urls(self, urls):
        # 判断添加进来的urls列表是否存在,且不为空
        for url in urls:
            self.add_new_url(url)
            # if url not in self.new_url and url and url not in self.old_url:
            #     self.new_url.append(url)

    # 判断是否还有可以爬取的url
    def has_new_url(self):

        return self.get_new_url_size() > 0

    # 获取可以爬取的数量
    def get_new_url_size(self):

        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):

        return len(self.old_url)

    pass

# 爬取数据
class Downloader(object):

    # 发送请求,返回响应数据
    def download(self, url):

        headers = {
            "User-Agent": UserAgent().chrome
        }

        response = requests.get(url, headers=headers)

        # 判断请求是否成功
        if response.status_code ==200:
            response.encoding = "gb2312"
            return response.text
            # return response.content.decode("utf-8")
        else:
            print("请求'{}'失败...".format(response.url))
            return None

    pass

# 解析数据
class ParsePage(object):

    # 根据html文档信息解析所需的数据
    def parse(self, html):

        # 使用lxml解析文档数据,xpath提取数据
        element = etree.HTML(html)

        # 提取数据并返回
        datas = self.parse_info(element)
        urls = self.parse_urls(element)

        return datas, urls

    def parse_info(self, element):

        divs = element.xpath("//div[@id='endtext']")
        datas = []

        for div in divs:
            datas.append(div.xpath("string(.)"))

        return datas

    def parse_urls(self, element):

        urls = element.xpath("//div[@id='ct_page']/ul/li/a/@href")
        urls = ["http://www.lovehhy.net{}".format(url) for url in urls]

        return urls

# 数据存储
class DataOutPut(object):

    def save(self, datas):
        with open("duanzi.txt", "a", encoding="utf-8") as ft:
            for data in datas:
                ft.write(data + "\n")


# 爬虫调度器
class SpiderDispatch(object):

    def __init__(self):
        self.urlmanager = URLManager()
        self.downloader = Downloader()
        self.parsepage = ParsePage()
        self.data_svae = DataOutPut()

    def run(self, url):

        # 程序开始首先添加一个url到URL管理器的列表(未爬取的url列表)
        self.urlmanager.add_new_url(url)

        # 判断url管理器是否有未爬取的url
        while self.urlmanager.has_new_url():

            # 从URL管理器的列表(未爬取的url列表)中获取一个url
            url = self.urlmanager.get_new_url()

            # 根据获取的url发送请求得到响应数据
            html = self.downloader.download(url)

            # 解析响应数据,返回所需数据及url
            datas, urls = self.parsepage.parse(html)

            # 保存数据, 管理已爬取url
            self.data_svae.save(datas)
            self.urlmanager.add_new_urls(urls)

    pass


if __name__ == '__main__':

    # 创建调度器对象,执行爬虫程序
    spider = SpiderDispatch()
    # url = "http://www.haoduanzi.com/category/?1-1.html"
    url = "http://www.lovehhy.net/Joke/Detail/QSBK/2"
    spider.run(url)

    # for url in range(1,8):  # 包头部包尾
    #     url = "http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum={}".format(str(i))
    #
    #     spider.run(url)

    pass

    # http://www.haoduanzi.com/category/?1-1.html

