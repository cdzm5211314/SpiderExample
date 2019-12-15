# -*- coding: utf-8 -*-
import scrapy


class Cd15lianjiaSpider(scrapy.Spider):
    name = 'cd_15lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/pg{}/'.format(num) for num in range(1, 2)]

    def parse(self, response):
        # 获取每页中具体房子的url链接
        house_urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()

        for url in house_urls:
            # 发送请求,响应房子的具体信息
            yield scrapy.Request(url, callback=self.parse_info)

    def parse_info(self, response):
        # print(response.text)

        # 根据房子的具体信息提取所需数据
        house_title = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        # 房子价钱
        house_price = response.xpath('concat(//span[@class="total"]/text(),//span[@class="unit"]/span/text())').extract_first()
        # house_price = response.xpath('//span[@class="total"]/text()').extract_first()
        # 房子没平米多少钱
        house_average = response.xpath('string(//span[@class="unitPriceValue"])').extract_first()
        # 房子所属小区名称
        house_community = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        # 房子所在区域
        house_region = response.xpath('concat(string(//div[@class="areaName"]/span[@class="info"]),//a[@class="supplement"]/text())').extract_first()

        # 房子的基本信息

        # 房子基本属性
        base_attribute_ul = response.xpath('//div[@class="base"]/div[@class="content"]/ul')
        house_apartment = base_attribute_ul.xpath('./li[1]/text()').extract_first()
        house_area = base_attribute_ul.xpath('./li[3]/text()').extract_first()
        house_orientation = base_attribute_ul.xpath('./li[7]/text()').extract_first()
        house_floor = base_attribute_ul.xpath('./li[2]/text()').extract_first()
        house_structure = base_attribute_ul.xpath('./li[8]/text()').extract_first()
        house_elevator = base_attribute_ul.xpath('./li[10]/text()').extract_first()
        house_heating = base_attribute_ul.xpath('./li[11]/text()').extract_first()
        house_renovation = base_attribute_ul.xpath('./li[9]/text()').extract_first()

        # 房子属性
        # 房子户型
        # house_apartment = response.xpath('//div[@class="base"]/div[@class="content"]//li[1]/text()').extract_first()
        # # 房子面积
        # house_area = response.xpath('//div[@class="base"]/div[@class="content"]//li[3]/text()').extract_first()
        # # 房子朝向
        # house_orientation = response.xpath('//div[@class="base"]/div[@class="content"]//li[7]/text()').extract_first()
        # # 房子楼层
        # house_floor = response.xpath('//div[@class="base"]/div[@class="content"]//li[2]/text()').extract_first()
        # # 房子结构
        # house_structure = response.xpath('//div[@class="base"]/div[@class="content"]//li[8]/text()').extract_first()
        # # 房子电梯比例
        # house_elevator = response.xpath('//div[@class="base"]/div[@class="content"]//li[10]/text()').extract_first()
        # # 房子供暖方式
        # house_heating = response.xpath('//div[@class="base"]/div[@class="content"]//li[11]/text()').extract_first()
        # # 房子装修
        # house_renovation = response.xpath('//div[@class="base"]/div[@class="content"]//li[9]/text()').extract_first()

        # 房子交易属性
        transaction_attribute_ul = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul')
        house_type = transaction_attribute_ul.xpath('./li[2]/span[2]/text()').extract_first()
        house_use = transaction_attribute_ul.xpath('./li[4]/span[2]/text()').extract_first()
        house_last_transaction_time = transaction_attribute_ul.xpath('./li[3]/span[2]/text()').extract_first()

        # 房子交易权属
        # house_type = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[2]/span[2]/text()').extract_first()
        # # 房子用途
        # house_use = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[4]/span[2]/text()').extract_first()
        # # 房子上次交易时间
        # house_last_transaction_time = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[3]/span[2]/text()').extract_first()

        # 5 + 8 + 3 = 16 个字段属性
        yield {
            "title": house_title,
            "price": house_price,
            "average": house_average,
            "community": house_community,
            "region": house_region,

            "apartment": house_apartment,
            "area": house_area,
            "orientation": house_orientation,
            "floor": house_floor,
            "structure": house_structure,
            "elevator": house_elevator,
            "heating": house_heating,
            "renovation": house_renovation,

            "type": house_type,
            "use": house_use,
            "last_transaction_time": house_last_transaction_time,
        }
