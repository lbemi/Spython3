# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsfspiderSpider(CSVFeedSpider):
    name = 'mycsfspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    headers = ['name', 'sex', 'addr', 'email']
    # delimiter = '\t'
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        i['name'] = row['name']
        print('name: %s'%i['name'])
        i['sex'] = row['sex']
        print(' sex: %s'%i['sex'])
        i['addr'] = row['addr']
        print('addr: %s'%i['addr'])
        i['email'] = row['email']
        print('email: %s'%i['email'])
        print("-"*50)
        return i
