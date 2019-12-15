# -*- coding: utf-8 -*-
import scrapy


class Cd07zolbizhiSpider(scrapy.Spider):
    name = 'cd_07zolbizhi'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/8392_104018_2.html']

    def parse(self, response):

        image_url = response.xpath('//img[@id="bigImg"]/@src').extract()
        # image_name = response.xpath('//a[@id="titleName"]').extract()
        image_name = response.xpath('string(//h3)').extract_first()

        yield {
            "image_urls": image_url,  # image_urls必须为一个列表
            "image_name": image_name,  # image_names图片的名称
        }

        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        # /bizhi/8392_104011_2.html

        # 判断是否有下一页
        if next_url.endswith(".html"):
            url = response.urljoin(next_url)  # 拼接图片URL地址
            yield scrapy.Request(url, callback=self.parse)


