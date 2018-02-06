# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request
class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg2-cid4011029.html']

    def parse(self, response):
        item = AutopjtItem()
        item['name'] = response.xpath('//a[@class="pic"]/@title').extract()
        print(item['name'])
        item['price'] = response.xpath('//span[@class="price_n"]/text()').extract()
        print(item['price'])
        item['link'] =  response.xpath('//a[@class="pic"]/@href').extract()
        print(item['link'])
        # item['comum'] = response.xpath('//a[@name="itemlist-review"]/text()').extract()
        # print(item['comum'])
        yield item
        for i in range(1, 5):
            url = 'http://category.dangdang.com/pg'+ str(i) + '-cid4011029.html'
            yield Request(url, callback=self.parse)