# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpjtPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='mypydb')

    def process_item(self, item, spider):
        cs = self.conn.cursor()
        print(">>>>mysql Insert>>>>>")
        name = item['name'][0]
        key = item['keywd'][0]
        print(name,'------',key)
        # sql = 'insert into mytb(title,keywd) VALUES('"+name+"', '"+key+"')'
        sql = 'insert into mytb(title, keywd) values("%s", "%s");' % (name, key)
        try:
            cs.execute(sql)
            self.conn.commit()
            print("Sucessful Insert!")
        except Exception as e:
            print(str(e))
        # res = self.conn.query(sql)
        # print(res)
        # self.conn.commit()
        #
        return item
    def close_spider(self,spider):
        self.conn.close()