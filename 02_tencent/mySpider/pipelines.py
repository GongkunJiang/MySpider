# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json


# class ItcastJsonPipeline(object):
#     def __init__(self):
#         self.filename = open("teacher.json", 'w')
#
#     def process_item(self, item, spider):
#         jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.filename.write(jsontext.encode('utf-8'))
#         return item
#
#     def close_spider(self, spider):
#         self.filename.close()


class TencentJsonPipeline(object):
    def __init__(self):
        self.file = open('tencent.json', 'w')
        # self.file = open('tencent.jsonl', 'w')
        # self.file = open('tencent.csv', 'w')
        # self.file = open('tencent.xml', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()
