# -*- coding:utf-8 -*-
# @Desc : 拉取进度条进行全部数据加载
# @Author : Administrator


from selenium import webdriver
import time
from lxml import etree


url = "https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%94%B5%E8%84%91&pvid=89cd9aa803f64a7b8d9a568794da46ff"

# 创建浏览器对象
browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")

# 发送请求
browser.get(url)

# 进度条拉取,动态加载全部数据, 使用js脚本
js = "document.documentElement.scrollTop=100000"        # chrome与firdox浏览器都适用
browser.execute_script(js)

# 等待几秒,让数据加载完成
time.sleep(5)

# 获取响应内容
html = browser.page_source

# 创建解析对象
htmlElement = etree.HTML(html)

prices = htmlElement.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]//i/text()')
names = htmlElement.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/@title')

print(len(names))
for name, price in zip(names, prices):
    print(name, price)
    # print(name.xpath("string(.)"), price)

# 关闭当前页面以及关闭浏览器
# driver.close()
# driver.quit()