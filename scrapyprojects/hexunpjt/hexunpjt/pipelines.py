# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HexunpjtPipeline(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'admin',
                db = 'hexun'
            )
        except ConnectionError as e:
            print(str(e))

    def process_item(self, item, spider):
        cour = self.conn.cursor()
        for j in range(0, len(item)):
            name = item['name'][j]
            url = item['url'][j]
            hits = item['hits'][j]
            comment = item['comment'][j]
            sql = 'insert into myhexun(name, url, hits, comment) values("%s","%s","%s","%s");'%(name, url, hits, comment)
            try:
                cour.execute(sql)
                self.conn.commit()
            except Exception as e:
                print('Insert Error--> ' + str(e))
        return item
    def close_spider(self,spider):
        self.conn.close()