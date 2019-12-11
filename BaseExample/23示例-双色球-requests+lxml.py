# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


# 开始日期: 2003年
# http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?beginIssue=2003001&endIssue=2019160
# http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum=7

from fake_useragent import UserAgent
import requests
from lxml import etree
import time
from random import randint
import pymysql

class ShuangSeQiuSpider(object):

    # def __init__(self, url):
    #     self.url = url
    #     self.headers = {"User-Agent":UserAgent().chrome}

    def __init__(self):
        self.headers = {"User-Agent":UserAgent().chrome}

    # def get_page_html(self):
    def get_page_html(self, url):

        # 发送请求
        time.sleep(randint(3, 5))  # 每次请求等待几秒
        # response = requests.get(self.url, headers=self.headers)
        response = requests.get(url, headers=self.headers)

        # 判断请求是否发送成功
        if response.status_code == 200:
            # 返回响应的信息
            return response.text
        else:
            print("此次请求失败...")

    def parse_page_info_zero(self, html):
        """提取每期的中奖号码-号码前面有0"""
        # 使用lxml解析响应的文档信息
        htmlElement = etree.HTML(html)

        # 使用xpath表达式提取数据
        trs = htmlElement.xpath("//tbody/tr")
        ssq_list = []
        for tr in trs:
            ssq_dict = {}
            # 返回是一个对象 lxml.etree._ElementUnicodeResult

            qihao = str(tr.xpath("./td[3]/text()")[0])  # 每期编号 转换为字符串
            hongqiu = tr.xpath("./td[4]/text()")[0].strip().split(" ")  # 中奖红球 转换为字符串并分割为字符串列表
            lanqiu = str(tr.xpath("./td[4]/span/text()")[0])  # 中奖篮球 转换为字符串
            # print(qihao, hongqiu, lanqiu)
            # print(type(qihao), type(hongqiu), type(lanqiu))

            # 把每期的中奖号码构建为一个字典
            ssq_dict = {
                "qihao": qihao,
                "redOne": hongqiu[0],
                "redTwo": hongqiu[1],
                "redThree": hongqiu[2],
                "redFour": hongqiu[3],
                "redFive": hongqiu[4],
                "redSix": hongqiu[5],
                "blueSeven": lanqiu,
            }

            # 把组成的每期字典数据存储在列表中
            ssq_list.append(ssq_dict)

        return ssq_list

    def parse_page_info_del_zero(self, html):
        """提取每期的中奖号码-号码前面无0"""
        # 使用lxml解析响应的文档信息
        htmlElement = etree.HTML(html)

        # 使用xpath表达式提取数据
        trs = htmlElement.xpath("//tbody/tr")
        ssq_list = []
        for tr in trs:
            ssq_dict = {}
            # 返回是一个对象 lxml.etree._ElementUnicodeResult

            qihao = str(tr.xpath("./td[3]/text()")[0])  # 每期编号 转换为字符串
            hongqiu = tr.xpath("./td[4]/text()")[0].strip().split(" ")  # 中奖红球 转换为字符串并分割为字符串列表
            lanqiu = str(tr.xpath("./td[4]/span/text()")[0])  # 中奖篮球 转换为字符串
            # print(qihao, hongqiu, lanqiu)
            # print(type(qihao), type(hongqiu), type(lanqiu))

            # 把每期的中奖号码构建为一个字典
            ssq_dict = {
                "qihao": qihao,
                "redOne": hongqiu[0].lstrip('0'),
                "redTwo": hongqiu[1].lstrip('0'),
                "redThree": hongqiu[2].lstrip('0'),
                "redFour": hongqiu[3].lstrip('0'),
                "redFive": hongqiu[4].lstrip('0'),
                "redSix": hongqiu[5].lstrip('0'),
                "blueSeven": lanqiu.lstrip('0'),
            }

            # 把组成的每期字典数据存储在列表中
            ssq_list.append(ssq_dict)

        return ssq_list

    def save_page_data(self):
        """保存数据"""
        pass

class MySQLHelper(object):
    config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "root",
        "db": "shuangseqiu",
        "charset":"utf8",

    }

    def __init__(self):
        self.connection = pymysql.connect(**MySQLHelper.config)
        self.cursor = self.connection.cursor()


if __name__ == '__main__':

    # url = "http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum=1"
    # ssq = ShuangSeQiuSpider(url)

    # 发送请求
    # html = ssq.get_page_html()
    # print(html)

    # 解析并提取数据
    # ssq_list = ssq.parse_page_info_zero(html)  # 中奖号码前面有0
    # print(ssq_list)
    # print("提取了{}期数据".format(len(ssq_list)))
    # ssq_list = ssq.parse_page_info_del_zero(html)  # 中奖号码前面无0
    # print(ssq_list)
    # print("提取了{}期数据".format(len(ssq_list)))

    ssq = ShuangSeQiuSpider()

    client = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="shuangseqiu")
    cursor = client.cursor()
    sql = "insert into ssq values(0,%s,%s,%s,%s,%s,%s,%s,%s)"

    for i in range(1,8):  # 包头部包尾
        url = "http://kaijiang.zhcw.com/lishishuju/jsp/ssqInfoList.jsp?czId=1&beginIssue=2003001&endIssue=2019160&currentPageNum={}".format(str(i))
        html = ssq.get_page_html(url)
        ssq_list = ssq.parse_page_info_zero(html)
        # print(len(ssq_list))
        for d in ssq_list:
            cursor.execute(sql, [d["qihao"],d["redOne"],d["redTwo"],d["redThree"],d["redFour"],d["redFive"],d["redSix"],d["blueSeven"]] )
            client.commit()

    cursor.close()
    client.close()
    pass


