# -*- coding: utf-8 -*-
import scrapy
from SpiderExample.items import MaoyanItem


class Cd03maoyanSpider(scrapy.Spider):
    name = 'cd_03maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://www.maoyan.com/films']

    def parse(self, response):


        moive_names = response.xpath('//div[@class="movies-list"]//div[@class="channel-detail movie-item-title"]/@title').extract()
        moive_urls = response.xpath('//div[@class="movies-list"]//div[@class="channel-detail movie-item-title"]/a/@href').extract()
        # scores_div = response.xpath('//div[@class="movies-list"]//div[@class="channel-detail channel-detail-orange"]')

        # print(moive_names, moive_urls, moive_scores)

        # moive_scores = []
        # for scores in scores_div:
        #     moive_scores.append(scores.xpath("string(.)").extract_first())

        moive_scores = [scores.xpath("string(.)").extract_first() for scores in response.xpath(
            '//div[@class="movies-list"]//div[@class="channel-detail channel-detail-orange"]')]

        # yield 只能推送 字典类型和item对象类型 数据到pipeline
        # for movie_name, movie_score, movie_url in zip(moive_names, moive_scores, moive_urls):
        #     # print(movie_name,movie_score,movie_url)
        #     # 推送字典数据到pipeline中
        #     yield {"name":movie_name, "score":movie_score, "url":movie_url}

        movie_item = MaoyanItem()
        for movie_name, movie_score, movie_url in zip(moive_names, moive_scores, moive_urls):
            # print(movie_name,movie_score,movie_url)

            movie_item["name"] = movie_name
            movie_item["score"] = movie_score
            movie_item["url"] = movie_url
            # 推送item数据到pipeline中
            yield movie_item

# 生成文件格式保存数据
# scrapy crawl cd_03maoyan -o movies.json
# scrapy crawl cd_03maoyan -o movies.csv
# scrapy crawl cd_03maoyan -o movies.xml