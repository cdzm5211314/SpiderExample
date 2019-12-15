# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderexampleItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


class MaoyanItem(scrapy.Item):

    # 爬取的数据字段名称
    name = scrapy.Field()
    score = scrapy.Field()
    url = scrapy.Field()

class Cd07zolbizhiItem(scrapy.Item):

    # 定义自动下载图片的两个字段属性
    image_urls = scrapy.Field()  # 存储下载图片的url地址,是一个列表
    images = scrapy.Field()  # 存储图片的相关信息

