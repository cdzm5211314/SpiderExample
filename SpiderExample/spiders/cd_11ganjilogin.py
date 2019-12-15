# -*- coding: utf-8 -*-
import scrapy
import re

class Cd11ganjiloginSpider(scrapy.Spider):
    name = 'cd_11ganjilogin'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):

        hash_code = re.findall(r'"__hash__":"(.+)"', response.text)[0]

        # check_url = response.xpath('//div[@class="form-div js-checkcode"]//img[@class="login-img-checkcode"]/@src').extract_first()  # 匹配是并不是response响应的数据

        check_url = response.xpath('//label/img/@data-url').extract_first()
        # check_url = "https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha"

        # 发送请求获取验证码
        yield scrapy.Request(check_url, callback=self.parse_check, meta={"hash_code":hash_code})

    def parse_check(self, response):

        hash_code = response.request.meta["hash_code"]

        with open("yzm.jpg", "wb",) as ft:
            # 把获取到验证码图片写入到本地
            ft.write(response.body)

        code = input("请输入验证码: ")

        login_data = {
            "username": "cd18103763930",
            "password": "chen123456",
            "setcookie": "14",
            "checkCode": code,
            "next": "/",
            "source": "passport",
            "__hash__": hash_code,
        }

        # 发送登录请求
        login_url = "https://passport.ganji.com/login.php"
        yield scrapy.FormRequest(login_url, formdata=login_data, callback=self.parse_login)


    def parse_login(self, response):

        print(response.text)