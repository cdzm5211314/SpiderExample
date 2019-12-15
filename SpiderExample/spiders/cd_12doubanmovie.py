# -*- coding: utf-8 -*-
import scrapy


class Cd12doubanmovieSpider(scrapy.Spider):
    name = 'cd_12doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ["https://movie.douban.com/top250?start={}&filter=".format(num*25) for num in range(10)]

    def parse(self, response):

        # 电影详解url地址
        movie_urls = response.xpath('//li//div[@class="info"]//a/@href').extract()
        # 电影名称
        movie_titles = response.xpath('//li//div[@class="info"]//a/span[1]/text()').extract()
        # 电影评分
        movie_scores = response.xpath('//li//div[@class="info"]//div[@class="star"]/span[2]/text()').extract()
        # 电影评论
        movie_comments = response.xpath('//li//div[@class="info"]//div[@class="star"]/span[4]/text()').extract()

        for movie_url, movie_title, movie_score, movie_comment in zip(movie_urls,movie_titles,movie_scores,movie_comments):
            movie_dict = {
                "url":movie_url,
                "title":movie_title,
                "score":movie_score,
                "comment":movie_comment,
            }

            yield movie_dict

            # yield {
            #     "url": movie_url,
            #     "title": movie_title,
            # }

