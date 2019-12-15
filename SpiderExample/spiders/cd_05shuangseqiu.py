# -*- coding: utf-8 -*-
import scrapy


class Cd05shuangseqiuSpider(scrapy.Spider):
    name = 'cd_05shuangseqiu'
    allowed_domains = ['kaijiang.zhcw.com']
    start_urls = [
        'http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum=1']

    def parse(self, response):

        qihaos = response.xpath("//tbody/tr/td[3]/text()").extract()  # 期号列表
        lanqius = response.xpath("//tbody/tr/td[4]/span/text()").extract()  # 篮球中奖号列表
        # hongses = response.xpath("//tbody/tr/td[4]/text()").extract()  # 红色中奖号列表

        # 获取经过处理的红球列表
        hongqius = [hongse.split(" ")[0:-1] for hongse in response.xpath("//tbody/tr/td[4]/text()").extract()]

        # print(qihaos,hongqius,lanqius)

        # 把期号,红球号,篮球号组成一个dict字典类型数据
        for index in range(len(qihaos)):
            ssq_dict = {
                "qihao": qihaos[index],
                # 取出的红球元素为每期中奖的红色球组成的列表
                "redOne": hongqius[index][0].lstrip('0'),
                "redTwo": hongqius[index][1].lstrip('0'),
                "redThree": hongqius[index][2].lstrip('0'),
                "redFour": hongqius[index][3].lstrip('0'),
                "redFive": hongqius[index][4].lstrip('0'),
                "redSix": hongqius[index][5].lstrip('0'),
                "blueSeven": lanqius[index].lstrip('0'),
            }

            yield ssq_dict

        # 获取下一页的url地址
        next_url = response.xpath('//div[@class="container"]/div[4]/a[3]/@href').extract_first().rstrip()
        # print(next_url)  # ssqInfoList.jsp?czId=1&amp;beginIssue=2003001&amp;endIssue=2019160&amp;currentPageNum=7

        # 拼接访问的url地址
        url = response.urljoin(next_url)
        print(url)  # http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum=2

        if url != response.url:
            # url地址不是最后一页就继续爬取
            yield  scrapy.Request(url, callback=self.parse)



