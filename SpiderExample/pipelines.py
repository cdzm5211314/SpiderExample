# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
import pymysql

class SpiderexamplePipeline(object):
    def process_item(self, item, spider):
        # print(spider.name)
        return item


class Cd03maoyanPipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""
        # 打开文件
        self.filename = open("movie.txt", "w", encoding="utf-8")


    def process_item(self, item, spider):
        # item数据类型跟爬虫文件yield推送过来的数据类型一致
        # print(type(item))

        # 把爬取的数写入到文件中(把字典类型数据转换为Json字符串类型)
        # self.filename.write(json.dumps(item, ensure_ascii=False) + "\n")

        # 把爬取的数写入到文件中(把item对象类型数据转换为字典类型然后再转换为Json字符串类型)
        item_dict = dict(item)
        self.filename.write(json.dumps(item_dict, ensure_ascii=False) + "\n")

        return item  # 如果开启了其他pipeline类,爬虫数据也会被其他的pipeline类所接受

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭文件
        self.filename.close()


class Cd04xbiqugePipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""
        # 打开文件
        self.filename = open("武炼巅峰.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):

        # 把爬取的数写入到文件中(把字典类型数据转换为Json字符串类型)
        title = item["title"]
        content = item["content"]

        # info = title + "\n" + content + "\n"
        info = title + "\n"

        self.filename.write(info)
        self.filename.flush()  # 手动把数据从内存中刷新出来(到硬盘)

        # return item

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭文件
        self.filename.close()


class Cd05shuangseqiuPipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""
        # 打开文件
        self.filename = open("双色球.txt", "w", encoding="utf-8")


    def process_item(self, item, spider):

        # 把爬取的数写入到文件中(把字典类型数据转换为Json字符串类型)
        info = json.dumps(item, ensure_ascii=False)

        self.filename.write(info + "\n")
        self.filename.flush()  # 手动把数据从内存中刷新出来(到硬盘)

        # return item

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭文件
        self.filename.close()

class Cd06xbiqugePipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""
        # 打开文件
        self.filename = open("武炼巅峰.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):

        title = item["title"]
        content = item["content"]

        # info = title + "\n" + content + "\n"
        info = title + "\n"

        self.filename.write(info)
        self.filename.flush()  # 手动把数据从内存中刷新出来(到硬盘)

        # return item

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭文件
        self.filename.close()


from scrapy.pipelines.images import ImagesPipeline
import scrapy
class Cd07zolbizhiPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            # 对各个图片URL返回一个Request
            yield scrapy.Request(image_url, meta={"image_name":item["image_name"]})

    def file_path(self, request, response=None, info=None):
        """ 给下载的图片自定义图片名称 """
        meta_dict = request.meta  # 获取Request传递过来的meta字典数据
        image_name = meta_dict["image_name"].strip().replace("\r\n\t\t","") + ".jpg"
        return image_name.replace("/","_")  # 返回图片名称及后缀名称

    def item_completed(self, results, item, info):

        pass


class Cd12doubanmoviePipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""

        # 连接mongodb
        # self.client = pymongo.MongoClient("localhost",27017)
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        # 添加数据之前先清空集合文档数据
        # self.client.douban.movie.delete_many({})
        self.client.douban.movie.remove({})
        print("集合文档数据已删除")

    def process_item(self, item, spider):

        # 插入数据
        self.client.douban.movie.insert_one(item)

        # return item

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭连接
        self.client.close()


class Cd15lianjiaPipeline(object):

    def open_spider(self, spider):
        """开启爬虫时执行,只执行一次"""

        # 连接mongodb
        # self.client = pymongo.MongoClient("localhost",27017)
        # self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        # 添加数据之前先清空集合文档数据
        # # self.client.lianjia.ershoufang.delete_many({})
        # self.client.lianjia.ershoufang.remove({})
        # print("集合文档数据已删除")

        # 链接mysql
        self.client = pymysql.connect(host="localhost",user="root", password="root", db="lianjia", port=3306, charset="utf8")
        self.cursor = self.client.cursor()

        # 添加数据之前清空表数据
        self.cursor.execute("delete from ershoufang")
        print("数据库表数据已删除")
        # self.cursor.execute("truncate table ershoufang")

    def process_item(self, item, spider):

        # 使用mongo插入数据
        # self.client.lianjia.ershoufang.insert_one(item)


        # 使用mysql插入数据
        args = [item["title"],item["price"],item["average"],item["community"],item["region"],item["apartment"],item["area"],item["orientation"],item["floor"],item["structure"],item["elevator"],item["heating"],item["renovation"],item["type"],item["use"],item["last_transaction_time"]]
        sql = "insert into ershoufang values (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, args=args)
        self.client.commit()

        # return item

    def close_spider(self, spider):
        """关闭爬虫时执行,只执行一次"""
        # 关闭连接
        self.cursor.close()
        self.client.close()