# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    book_name = scrapy.Field()
    ID_name = scrapy.Field()
    comment = scrapy.Field()
