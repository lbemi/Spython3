# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
class MyfirstpjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("./home.txt","wb",encoding='utf-8')

    def process_item(self, item, spider):
        l = str(item)+'\n'
        print(l)
        self.file.write(l)
        return item

    def close_spider(self, spider):
        self.file.close()