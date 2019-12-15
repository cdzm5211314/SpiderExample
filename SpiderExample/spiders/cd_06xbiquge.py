# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Cd06xbiqugeSpider(CrawlSpider):
    name = 'cd_06xbiquge'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/0/10/']  # 目录
    # start_urls = ['http://www.xbiquge.la/0/10/7109.html']  # 第一章

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[1]/a'), callback='parse_item', follow=True),
        # 定义URL链接匹配规则(XPath表达式) ---> 结果显示没有第一章,所以可以在定义一个规则提取第一章的URL链接
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        title = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            "title": title,
            "content": content,
        }


