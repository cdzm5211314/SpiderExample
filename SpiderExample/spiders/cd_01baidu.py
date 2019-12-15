# -*- coding: utf-8 -*-
import scrapy


class Cd01baiduSpider(scrapy.Spider):
    name = 'cd_01baidu'  # 保证爬虫名称的唯一性
    allowed_domains = ['baidu.com']  # 允许爬取的域名
    start_urls = ['http://www.baidu.com/']  # 爬虫的起始url

    def parse(self, response):

        print(response.text)
