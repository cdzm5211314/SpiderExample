# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

from threading import Thread
from queue import Queue
import time
from fake_useragent import UserAgent
import requests
from lxml import etree


## Python提供了队列操作: 模块queue ---> 类Queue
# Queue: FIFO先入先出
# LifoQueue: FIFO后入先出
# PriorityQueue: 优先级

## 队列对象方法: Queue(maxsize) - 创建一个先进先出的队列
# Queue.qsize()                                 返回队列的大小
# Queue.empty()                                 判断队列是否为空,队列为空返回True
# Queue.full()                                  判断队列是否满了,队列满了返回True
# Queue.get(item, block=True, timeout=None)     从队列里取数据
# Queue.put(item, block=True, timeout=None)     往队列里放数据
# Queue.join()                                  一直阻塞,直到队列中的所有元素都被取出和执行
# Queue.put_nowait(item)                        往队列里存放元素，不等待
# Queue.get_nowait(item)                        从队列里取元素，不等待
# Queue.task_done()                             清除任务:从queue中取出一个任务,然后清除一下任务


# 多线程: threading.Thread 类
# 创建线程的两种方式(方法与类继承)
# 第一种: 方法
# 1.定义一个方法
# def test(num):
#     print("线程: " + num)
#     time.sleep(2)

# 2.创建线程
# def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
# 参数说明: name表示线程名称,默认为Thread-1, target表示线程函数, args表示给线程函数位置传参(元组类型), kwargs给线程函数键值传参(字典类型)
# t1 = Thread(target=test, args=("001",))
# t2 = Thread(target=test, kwargs={"num": "002"})

# 3.启动线程
# t1.start()
# t2.start()

# 第二种: 类继承
# 1.定义一个类并继承Thread
# class MyThread(Thread):
#     def __init__(self, num):
#         # 2.加载Thread父类中的__init__方法
#         super(MyThread, self).__init__()
#         self.num = num

    # 3.重写父类的run方法
    # def run(self):
    #     print("线程: " + self.num)
    #     time.sleep(2)

# 4.创建线程
# mt1 = MyThread("003")
# mt2 = MyThread("004")

# 5.开启线程
# mt1.start()
# mt2.start()

##############################################################################################
# 爬虫类
class SpiderInfo(Thread):

    def __init__(self, url_queue, info_queue):
        # super(SpiderInfo,self).__init__()
        Thread.__init__(self)
        self.url_queue = url_queue
        self.info_queue = info_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().chrome
        }

        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            print(response.url,response.status_code)
            if response.status_code == 200:
                self.info_queue.put(response.text)

# 解析类
class ParseInfo(Thread):
    def __init__(self, info_queue):
        super(ParseInfo, self).__init__()
        self.info_queue = info_queue

    def run(self):
        while self.info_queue.empty() == False:
            htmlElement = etree.HTML(self.info_queue.get())
            # titles = htmlElement.xpath("//div[@id='footzoon']/h3/a")
            contents_list = htmlElement.xpath("//div[@id='footzoon']/div[@id='endtext']")
            # print(titles, contents)
            with open("xiaohua.txt", "a", encoding="utf-8") as f:
                for content in contents_list:
                    # content = content.xpath("./text()")
                    content = content.xpath("string(.)").strip()
                    f.write(content + "\n")


if __name__ == '__main__':

    # 存储url的容器
    url_queue = Queue()
    base_url = "http://www.lovehhy.net/Joke/Detail/QSBK/{}"
    for num in range(1, 11):
        url_queue.put(base_url.format(num))

    # 存储内容的容器
    info_queue = Queue()

    # 创建一个爬虫类对象
    # spider = SpiderInfo(url_queue)
    # spider.start()

    # 创建多个爬虫类对象
    spider_list = []
    for i in range(1, 3):
        spider = SpiderInfo(url_queue, info_queue)
        spider_list.append(spider)
        spider.start()

    for spider in spider_list:
        spider.join()

    # 创建一个解析类
    parse = ParseInfo(info_queue)
    parse.start()

    # 创建多个解析类对象
    parse_list = []
    for i in range(1, 3):
        parse = ParseInfo(info_queue)
        parse_list.append(parse)
        parse.start()

    for parse in parse_list:
        parse.join()


