# -*- coding: utf-8 -*-
import scrapy
from saveproject.items import SaveprojectItem

class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    allowed_domains = ['sina.com']
    start_urls = ['http://mil.news.sina.com.cn/jssd/2018-02-05/doc-ifyreyvz9127776.shtml',
                  'http://news.sina.com.cn/gov/xlxw/2018-02-06/doc-ifyremfz5717244.shtml']

    def parse(self, response):
        item = SaveprojectItem()
        item['title'] = response.xpath('/html/head/title').extract()
        item['key'] = response.xpath('//meta[@name="keywords"]/@content').extract()
        print(item['title'])
        print(item['key'])
        yield item  # 不添加这句，piplines中的 ’process_item‘ 不会执行