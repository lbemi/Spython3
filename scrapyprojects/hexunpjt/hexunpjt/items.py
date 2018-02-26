# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    hits = scrapy.Field()
    comment = scrapy.Field()