# -*- coding: utf-8 -*-
import scrapy


class Cd10renrenloginSpider(scrapy.Spider):
    name = 'cd_10renrenlogin'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    def start_requests(self):

        url = "http://www.renren.com/893394172/profile"
        cookie_str = "anonymid=k456ongu-692yve; depovince=GW; _r01_=1; JSESSIONID=abc1b1dYlXXUC62uCcd8w; ick_login=e969f6d3-b2ce-47ef-a79d-2981e86465d9; _de=3F1C6150E59B993580B4C5FE015D8D28; jebecookies=d72979f1-3b8b-46c3-bba0-e81e56a06736|||||; p=641994e0ad07ad56e7bd21713166649d2; first_login_flag=1; ln_uact=18103763930; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=63f17c8778f1244d8fe49a8e498526202; societyguester=63f17c8778f1244d8fe49a8e498526202; id=893394172; xnsid=fcdbe2d4; ver=7.0; loginfrom=null; jebe_key=fb00eda7-8a9e-441c-99b3-0ca11d3a314b%7C5b34e73601acb25887c4068b9cf69955%7C1576305706853%7C1%7C1576305708493; wp_fold=0"
        cookie_dict = {}

        for cookievalue in cookie_str.split("; "):  # 根据"; "进行分割cookie字符串组成一个列表
            key, value = cookievalue.split("=")  # 根据"="进行分割每个cookie的键与值
            cookie_dict[key] = value
        # print(cookie_dict)
        yield scrapy.Request(url, cookies=cookie_dict, callback=self.parse)


    def parse(self, response):

        # 提取所需要的数据
        author = response.xpath('//h1[@class="avatar_title no_auth"]/text()').extract_first().strip()

        print(author)
