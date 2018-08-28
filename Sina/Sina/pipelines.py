# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import sys

class SinaPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']
        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrls[-30:-6].replace('/', '_')
        filename += ".txt"
        print filename
        fp = open(item['subFilename'] + '/' + filename, 'w')
        # fp.write(item['parentTitle'])
        # fp.write(item['parentUrls'])
        # fp.write(item['subTitle'])
        # fp.write(item['subUrls'])
        # fp.write(item['subFilename'])
        fp.write(item['sonUrls'])
        # fp.write(item['head'])
        # fp.write(item['content'])

        fp.close()

        return item
