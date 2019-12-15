# -*- coding: utf-8 -*-
import scrapy


class Cd08httpUaSpider(scrapy.Spider):
    name = 'cd_08http_ua'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):

        # 测试随机获取的User-Agent
        import json
        d = json.loads(response.text)
        print(d['headers']['User-Agent'])

        # 测试动态代理IP
        d = json.loads(response.text)
        print(d['origin'])


