# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# 爬虫中间件
class SpiderexampleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 下载中间件
class SpiderexampleDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 编写User-Agen的DownloaderMiddleware下载中间件
from fake_useragent import UserAgent
from random import choice
# from SpiderExample.settings import USER_AGENTS
class UserAgentDownloaderMiddleware(object):

    def process_request(self, request, spider):

        # 设置随机的获取User-Agent
        # request.headers.setdefault(b'User-Agent', UserAgent().chrome) # 随机chrome浏览器任意版本
        request.headers.setdefault(b'User-Agent', UserAgent().random) # 随机任意浏览器任意版本
        # request.headers.setdefault(b'User-Agent', choice(USER_AGENTS))


# 编写动态代理IP的DownloaderMiddleware下载中间件
class ProxyDownloaderMiddleware(object):

    def process_request(self, request, spider):

        # 设置动态代理IP
        # request.meta['proxy'] = "http://ip:port"
        # request.meta['proxy'] = "http://username:password@ip:port"
        request.meta['proxy'] = "http://61.153.251.150:22222"


# Selenium + Scrapy 结合使用
from selenium import webdriver
from scrapy.http import HtmlResponse
class SeleniumDownloaderMiddleware(object):

    # def __init__(self):
    #
    #     # 创建浏览器对象 - chrome浏览器出现问题
    #     # self.browser = webdriver.Chrome(executable_path="E:\Installation_Tools\Driver\ChromeDriver\chromedriver.exe")
    #     self.browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        url = request.url  # 请求要访问的url链接

        # 每次请求都会去创建一个浏览器对象
        # browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")

        # 发送请求
        # self.browser.get(url)

        # 获取响应的内容
        # html = self.browser.page_source

        spider.browser.get(url)
        html = spider.browser.page_source

        # print(html)

        # HtmlResponse对象,它是Response的子类,返回之后便顺次调用每个Downloader Middleware的process_response()方法
        # 而在process_response()中我们没有对其做特殊处理,它会被发送给Spider,传给Request的回调函数进行解析
        return HtmlResponse(url, body=html, request=request, encoding="utf-8")

    def process_response(self, request, response, spider):

        return response

    def process_exception(self, request, exception, spider):

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


