# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/2103151045.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        i['title'] = response.xpath('/rss/channel/item/title/text()').extract()
        i['link'] = response.xpath('/rss/channel/item/link/text()').extract()
        i['author'] = response.xpath('/rss/channel/item/author/text()').extract()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        for j in range(len(i['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题："+ i['title'][j])
            print("链接："+ i['link'][j])
            print("作者："+ i['author'][j])
            print("-"*80)
        return i
