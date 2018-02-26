# -*- coding: utf-8 -*-

from hexunpjt.items import HexunpjtItem
from  scrapy.http import Request
import scrapy
import re
import urllib.request
import http.cookiejar
c = http.cookiejar.CookieJar()


class MyhexunspdSpider (scrapy.Spider):
    # print(">>>>>>MyhexunspdSpider>>>>")
    name = 'myhexunspd'
    uid = '26325289'
    allowed_domains = ['hexun.com']
    start_urls = ['http://hexun.com/']

    def start_requests(self):
        # print(">>>>start_requests>>>>>")
        yield Request ("http://" + str (self.uid) + ".blog.hexun.com/p1/default.html",
                       headers={
                           "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
                       })

    def parse(self, response):
        item = HexunpjtItem ()
        item['name'] = response.xpath ('//span[@class="ArticleTitleText"]/a/text()').extract()
        # print(item['name'])
        item['url'] = response.xpath ('//span[@class="ArticleTitleText"]/a/@href').extract()
        # print (item['url'])
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)"' #抓取点击数及评论数网址
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        # hcurl = h.split('&')[0]
        # print(hcurl)
        header = (
            "User-agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        )
        opener = urllib.request.build_opener()
        opener.addheaders = [header]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(hcurl).read()
        # print(data)
        pat2 = "click\d*?','(\d*?)'" #获取点击量
        pat3 = "comment\d*?','(\d*?)'"#获取评论数
        item['hits'] = re.compile(pat2).findall(str(data))
        # print(item['hits'])
        item['comment'] = re.compile(pat3).findall(str(data))
        # print (item['comment'])
        yield item

        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))
        if(len(data2) >= 2):
            totalurl = data2[-2]
        else:
            totalurl = 1
        for i in range(2, int(totalurl)+1):
            nexturl = "http://" + str (self.uid) + ".blog.hexun.com/p" + str(i) + "/default.html"
            yield Request(nexturl, callback=self.parse, headers={
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
            })