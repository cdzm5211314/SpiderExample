# -*- coding: utf-8 -*-
import scrapy


class Cd02qidianSpider(scrapy.Spider):
    name = 'cd_02qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/finish?chanId=4']

    def parse(self, response):

        # 提起数据
        book_names = response.xpath('//div[@class="book-mid-info"]/h4/a/text()').extract()
        book_urls = response.xpath('//div[@class="book-mid-info"]/h4/a/@href').extract()
        book_authors = response.xpath('//div[@class="book-mid-info"]/p/a[1]/text()').extract()

        # print(book_names, book_authors, book_urls)

        book_info = []
        for book_name, book_author, book_url in zip(book_names,book_authors,book_urls):
            # 定义书籍的字典信息
            book_info.append({"name":book_name, "author":book_author, "url":book_url})

        return book_info


