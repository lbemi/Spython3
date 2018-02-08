# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpjtPipeline(object):
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', passwd='admin', db='mypydb')

    def process_item(self, item, spider):
        title =  item['title'][0]
        keywd =  item['keywd'][0]
        # sql = 'insert into mytb(titile, keywd) VALUES ('"+name+"', '"+key+"' )'
        sql =  'insert into mytb(title,keywd) VALUES (title , keywd)'
        self.con.query(sql)
        return item
    def close_spider(self):
        self.con.close()