# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

import re

class ZhihuPipeline(ImagesPipeline):

    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

    def get_media_requests(self,item,info):
        #for image_url in item['image_urls']:
        for i, image_url in enumerate(item['image_urls']):
            #print 'i is:', i
            #print 'image_url is, ', image_url
            #print "item: titile", item['title']


            yield scrapy.Request(image_url, meta={'title': item['title'][i]}, dont_filter=False)


    def set_filename(self, key, response):
        #print 'response.meta: ', response.meta['title']
        #return 'full/{0}.jpg'.format(response.meta['title'][0])
        return 'full/' + response.meta['title'].split('.')[-1] + '.jpg'
        #return 'full/0001.jpg'

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    # def get_images(self,response, request, info):
    #     for key, image, buf in super(ZhihuPipeline, self).get_images(\
    #             response,request,info):
    #         x = 1
    #
    #     #yield key, image, buf
    #
    #     key = self.set_filename(response)
    #     yield key, image, buf

    def get_images(self, response, request, info):
        #print "get_images"

        for key, image, buf, in super(ZhihuPipeline, self).get_images(response, request, info):
            if self.CONVERTED_ORIGINAL.match(key):
                #print 'key is: ', key

                #print 'response is: ', response
                key = self.set_filename(key, response)
                #print 'new key is', key
            yield key, image, buf