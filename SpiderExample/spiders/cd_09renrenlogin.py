# -*- coding: utf-8 -*-
import scrapy


class Cd09renrenloginSpider(scrapy.Spider):
    name = 'cd_09renrenlogin'
    allowed_domains = ['renren.com']

    # start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        login_url = "http://www.renren.com/PLogin.do"
        login_data = {
            "email": "1810376****",
            "password": "ch**123***",
        }
        yield scrapy.FormRequest(login_url, formdata=login_data, callback=self.parse)

    def parse(self, response):

        # print(response.text)

        # 登录成功后再次发送请求
        info_url = "http://www.renren.com/893394172/profile"
        yield scrapy.Request(info_url, callback=self.parse_info)


    def parse_info(self,response):

        # 提取所需要的数据
        author = response.xpath('//h1[@class="avatar_title no_auth"]/text()').extract_first().strip()

        print(author)