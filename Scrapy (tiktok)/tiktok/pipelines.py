# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import os

class TiktokPipeline(FilesPipeline):
    def process_item(self, item, spider):
        return item
        
    def file_path(self, request, response=None, info=None):
        url = request if not isinstance(request, Request) else request.url
        media_guid = hashlib.sha1(to_bytes(url)).hexdigest()
        path, media_ext = os.path.splitext(url)
        media_name = os.path.split(path)[1]
        return '%s_%s%s' % (media_name, media_guid, ".mp4")
    
    # def file_path(self, request, response = None, info = None):
        # url = request.url
        ## change to request.url after deprecation
        ## media_ext = os.path.splitext(url)[1]
        # return 'full/%s.mp4' % (request.meta['filename'])


