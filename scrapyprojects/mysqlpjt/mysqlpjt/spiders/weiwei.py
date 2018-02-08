# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import CrawlSpider, Rule
from mysqlpjt.items  import MysqlpjtItem
class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/c/nd/2018-02-08/doc-ifyrkzqq9442352.shtml',
                  'http://news.sina.com.cn/c/nd/2018-02-07/doc-ifyrkzqq9395737.shtml'
                  ]

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.doc-.*?shtml'),allow_domains=('sina.com.cn')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('>>>>>>>>parse_item')
        item = MysqlpjtItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        print(item['title'])
        item['keywd'] = response.xpath('/html/head/meta[@name="Keywords"]/@content').extract()
        print(item['keywd'])
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
