import scrapy
import bs4
class DoubanSpider(scrapy.Spider):#继承scrapy.spider类
    name='douban'#启动爬虫的时候使用
    allowed_domains=['https://book.douban.com']
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self,response):#parse是Scrapy里默认处理response的一个方法，中文是解析;无requests.get(),因为scrapy框架代劳了做这件事
        bs = bs4.BeautifulSoup(response.text,'html.parser')#用BeautifulSoup解析response。
        datas = bs.find_all('tr',class_="item")#用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        for data in  datas:#遍历data。
            item = DoubanItem()
            #实例化DoubanItem这个类。
            item['title'] = data.find_all('a')[1]['title']
            #提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['publish'] = data.find('p',class_='pl').text
            #提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['score'] = data.find('span',class_='rating_nums').text
            #提取出评分，并把这个数据放回DoubanItem类的score属性里。
            print(item['title'])
            #打印书名。
            yield item
            #yield item是把获得的item传递给引擎。
