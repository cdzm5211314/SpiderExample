# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class Cd13splashScrapySpider(scrapy.Spider):
    name = 'cd_13splash_scrapy'
    allowed_domains = ['guazi.com']

    # start_urls = ['https://www.guazi.com/bj/buy/']

    def start_requests(self):

        url = "https://www.guazi.com/bj/buy/"

        # 第一种使用render.html源代码的方式
        # yield SplashRequest(url, callback=self.parse, args={"wait":1})  # args设置参数,wait等待1秒

        # 第二种使用execute(Lua脚本)的方式
        lua_script = """
            function main(splash, args)
              splash:go(args.url)
              splash:wait(1)
              return splash:html()
            end
        """
        yield SplashRequest(url, callback=self.parse, endpoint="execute", args={"lua_source":lua_script})

    def parse(self, response):

        print(response.text)


