# -*- coding:utf-8 -*-
# @Desc : 获取下一页标签元素点击进行下一页操作
# @Author : Administrator


from selenium import webdriver
import time

url = "https://www.huya.com/g/cf"

# 创建浏览器对象

# browser = webdriver.Chrome(executable_path="E:\Installation_Tools\Driver\ChromeDriver\chromedriver.exe")  # chrome浏览器出现问题
browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")

# 发送请求访问url地址
browser.get(url)

num = 1
while True:

    print("第" + str(num) + "页内容 -----> ")
    num += 1

    # 睡眠5秒等待页面加载完成
    time.sleep(5)

    # 获取响应的内容信息
    html = browser.page_source
    # print(html)

    # 使用selenium自带的数据提取功能
    names = browser.find_elements_by_xpath("//i[@class='nick']")     # 标签
    counts = browser.find_elements_by_xpath("//i[@class='js-num']")  # 标签

    # for name, count in zip(names, counts):
    #     print(name.text, count.text)

    # 判断是否有下一页的标签
    if browser.page_source.find("laypage_next") != -1:  # 说明有下一页
        # 获取下一页的标签
        element = browser.find_element_by_xpath("//a[@class='laypage_next']")
        # 鼠标点击进行下一页
        element.click()
    else:
        break


# 关闭当前页面以及关闭浏览器
# driver.close()
# driver.quit()
