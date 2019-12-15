# -*- coding: utf-8 -*-
import scrapy

# 爬取小说,为了保证章节顺序完整,进入首章节爬取章节内容,然后在首章节中提取下一章的url,然后再次爬取章节内容

class Cd04xbiqugeSpider(scrapy.Spider):
    name = 'cd_04xbiquge'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/0/10/7109.html']

    def parse(self, response):

        title = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            "title": title,
            "content": content,
        }

        # 下一章节的url提取
        next_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first()
        # /0/10/7110.html

        # 判断是否有下一章节
        # if next_url.endswith(".html"):
        if next_url.find(".html") != -1:
            # url = "http://www.xbiquge.la/0{}".format(next_url)
            url = response.urljoin(next_url)  # 自动补全url前面的内容
            yield scrapy.Request(url, callback=self.parse)



