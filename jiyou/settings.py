FEED_URI='./storage/data/%(name)s.csv'
FEED_FORMAT='CSV'
FEED_EXPORT_ENCODING='ansi'
#存储成excel文件的设置方法:只要取消ITEM_PIPELINES的注释（删掉#）即可。
#需要修改`ITEM_PIPELINES`的设置代码：

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#     'jobuitest.pipelines.JobuitestPipeline': 300,
# }

#需要修改的默认设置:

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5#下载时间不宜过快
