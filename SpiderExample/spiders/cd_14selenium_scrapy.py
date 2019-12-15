# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from selenium import webdriver

class Cd14seleniumScrapySpider(scrapy.Spider):
    name = 'cd_14selenium_scrapy'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/bj/buy/']


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Cd14seleniumScrapySpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider


    def spider_closed(self, spider):
        print("爬虫结束了...关闭浏览器")
        spider.browser.quit()  # 关闭浏览器


    def parse(self, response):

        print(response.text)

