# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = Field()
    images = Field()
    title = Field()
    #image_paths = Field()



