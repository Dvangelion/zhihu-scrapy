# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from zhihu.items import ZhihuItem
import re

class ExampleSpider(CrawlSpider):
    name = 'pic'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/topic/19643259/hot']
    #item = ZhihuItem()

    rules = [
        Rule(LinkExtractor(allow=['/question/.*','/people/.*']),
        callback = 'parse_item',
        follow = True)
    ]


    def parse_item(self, response):
        #print response.css('h1').extract()
        image = ZhihuItem()
        #head_url = re.sub(r'_l\.', '.', ''.join(response.css('.body .Avatar--l::attr(src)').extract()))


        image['title'] = response.xpath("//img/@alt").extract()
        #image['image_urls'] = arr
        rel = response.xpath("//img/@srcset").extract()
        #print 'adsfaksjdfawp9eifh', rel
        #print 'asdkfaiehfkajsbdfj', rel[0]

        for i in range(len(rel)):
            rel[i] = re.sub(' 2x','',rel[i])
        image['image_urls'] = rel

        #rel[0] = re.sub(' 2x','',rel[0])
        #image['image_urls'] = [rel[0]]
        #print image['image_urls']
        return image

