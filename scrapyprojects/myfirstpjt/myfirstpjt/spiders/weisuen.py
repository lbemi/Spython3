import scrapy

from myfirstpjt.items import MyfirstpjtItem

uu= 'http://blog.sina.com.cn/weiweihappy321'
class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = "sina.com.cn"
    start_urls =  ('http://slide.news.sina.com.cn/slide_1_86058_237641.html#p=1',
                   'http://news.sina.com.cn/china/xlxw/2018-01-30/doc-ifyqyesy4446142.shtml',
                   'http://k.sina.com.cn/article_2019120665_78595619034006wth.html?cre=sinapc&mod=g&loc=9&r=0&doct=0&rfunc=86&tj=none',)
    # urls2 =('http://www.jd.com',
    #         'http://sina.com.cn',
    #         'http://yum.iqianyue.com',
    #         )
    # def start_requests(self):
    #     for url in self.urls2:
    #         yield self.make_requests_from_url(url)

    # def __init__(self,  myurl=None, *args, **kwargs):
    #     super(WeisuenSpider, self).__init__(*args, **kwargs)
    #     myurllist =  myurl.split('|')
    #     for url in myurllist:
    #         print("爬取网址：%s" % url )
    #     self.start_urls = myurllist

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print(item['urlname'])