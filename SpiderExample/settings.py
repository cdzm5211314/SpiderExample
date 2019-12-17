# -*- coding: utf-8 -*-

# Scrapy settings for SpiderExample project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpiderExample'

SPIDER_MODULES = ['SpiderExample.spiders']
NEWSPIDER_MODULE = 'SpiderExample.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 设置请求头信息(模拟客户端浏览器):
#USER_AGENT = 'SpiderExample (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"

# USER_AGENTS = [
#    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
#    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
# ]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 设置成False,是拒绝遵守Robot协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 请求并发数(默认16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 限制下载频率(秒)
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# cookie默认开启状态
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认的请求头信息,也可以添加User-Agent头信息:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 爬虫中间件
SPIDER_MIDDLEWARES = {
   # 'SpiderExample.middlewares.SpiderexampleSpiderMiddleware': 543,
   # 'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载器中间件
DOWNLOADER_MIDDLEWARES = {
   # 'SpiderExample.middlewares.SpiderexampleDownloaderMiddleware': 543,
   # 数值越小表示优先级越高,默认543
   'SpiderExample.middlewares.UserAgentDownloaderMiddleware': 343,
   # 'SpiderExample.middlewares.ProxyDownloaderMiddleware': 243,
   # 'scrapy_splash.SplashCookiesMiddleware': 723,
   # 'scrapy_splash.SplashMiddleware': 725,
   # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  # 不配置查不到信息
   # 'SpiderExample.middlewares.SeleniumDownloaderMiddleware': 343,  # Selenium+Scrapy结合使用,定义中间件
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 管道
ITEM_PIPELINES = {
   # 'SpiderExample.pipelines.SpiderexamplePipeline': 300,
   # 'SpiderExample.pipelines.Cd03maoyanPipeline': 300,
   # 'SpiderExample.pipelines.Cd04xbiqugePipeline': 300,
   # 'SpiderExample.pipelines.Cd05shuangseqiuPipeline': 300,
   # 'SpiderExample.pipelines.Cd06xbiqugePipeline': 300,
   # 'scrapy.pipelines.images.ImagesPipeline': 300,  # 使用scrapy自带的pipeline下载图片
   # 'SpiderExample.pipelines.Cd07zolbizhiPipeline': 300,  # 使用自定义的pipeline下载图片,图片名称自定义
   # 'SpiderExample.pipelines.Cd12doubanmoviePipeline': 300,
   # 'SpiderExample.pipelines.Cd15lianjiaPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline' : 300,  # 分布式爬虫配置项

}

# 配置图片的下载路径
# IMAGES_STORE = "./img"  # 即当前项目根目录下的img目录,自动下载的时候会在img目录前加一个full目录

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

############################################################################################

# 日志信息(logging)设置:
# 日志的级别(从高到低): CRITICAL(严重错误) ERROR(一般错误) WARNING(警告) INFO(一般信息) DEBUG(调试信息)[默认级别]
# LOG_ENABLED = True  # 默认,日志信息的开关状态,设置为False为关闭状态
# LOG_LEVEL = 'DEBUG'  # 默认,日志信息的级别
# LOG_ENCODING = "utf-8"  # 默认,日志信息的编码格式
# LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'  # 默认,日志信息的数据格式
# LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'  # 默认,日志信息的日期时间格式
# LOG_STDOUT = 'False'  # 默认,如果设置为True,进程所有的标准输出(及错误)将会被重定向到log中
# LOG_FILE = None  # 默认,日志信息的输出文件名,如果设置为None,则使用标准错误输出(standard error)

# 日志信息文件的目录结构
# import datetime
# CURRENT_TIME = datetime.datetime.now()  # 获取当前时间current_time
# LOG_FILE_PATH = 'logs/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year,CURRENT_TIME.month,CURRENT_TIME.day)
# LOG_FILE = LOG_FILE_PATH  # 日志信息的存储文件位置,设置后终端不会显示日志信息



### Splash与Scrapy结合使用:
# 安装的Docker中Splash地址
# SPLASH_URL = "http://192.168.59.130:8050/"
# 配置消息队列所使用的过滤类
# DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
# 配置消息队列所使用的类
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'



### scrapy-redis分布式爬虫配置:
# REDIS_URL = 'redis://127.0.0.1:6379/2'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
