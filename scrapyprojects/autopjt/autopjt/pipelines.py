# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class AutopjtPipeline(object):

    def __init__(self):
        self.file = codecs.open('data.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        print(">>>>>process_item")
        # line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(line)
        for j in range(0,len(item['name'])):
            name =  item['name'][j]
            price = item['price'][j]
            link = item['link'][j]
            goods = {'name':name, 'price':price, 'link':link}
            line =  json.dumps(dict(goods), ensure_ascii=False) + '\n'
            self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()