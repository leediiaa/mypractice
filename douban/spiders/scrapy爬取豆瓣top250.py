#爬虫（Spiders）会把豆瓣的10个网址封装成requests对象，引擎会从爬虫（Spiders）里提取出requests对象，再交给调度器（Scheduler），让调度器把这些requests对象排序处理。
#然后引擎再把经过调度器处理的requests对象发给下载器（Downloader），下载器会立马按照引擎的命令爬取，并把response返回给引擎。
#紧接着引擎就会把response发回给爬虫（Spiders），这时爬虫会启动默认的处理response的parse方法，解析和提取出书籍信息的数据，使用item做记录，返回给引擎。引擎将它送入Item Pipeline（数据管道）处理。




#到这里，我们就用代码编写好了一个爬虫。不过，实际运行的话，可能还是会报错。
#原因在于Scrapy里的默认设置没被修改。比如我们需要修改请求头。点击settings.py文件，你能在里面找到如下的默认设置代码：
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
#请你把USER _AGENT的注释取消（删除#），然后替换掉user-agent的内容，就是修改了请求头。
#又因为Scrapy是遵守robots协议的，如果是robots协议禁止爬取的内容，Scrapy也会默认不去爬取，所以我们还得修改Scrapy中的默认设置。
#把ROBOTSTXT_OBEY=True改成ROBOTSTXT_OBEY=False，就是把遵守robots协议换成无需遵从robots协议，这样Scrapy就能不受限制地运行。
