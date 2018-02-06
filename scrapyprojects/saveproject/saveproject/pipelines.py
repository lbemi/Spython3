# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
class SaveprojectPipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('./test.json','wb',encoding='utf-8')
        print('open---')


    def process_item(self, item, spider):
        print("process_item")
        # l = str(item['title']) + '\n'
        # print(l)
        # self.file.write(l)

        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()
        print('colse---')