# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        # # 获取setting主机名、端口号和数据库名
        # host = settings['MONGODB_HOST']
        # port = settings['MONGODB_PORT']
        # dbname = settings['MONGODB_DBNAME']
        #
        # # pymongo.MongoClient(host, port) 创建MongoDB链接
        # client = pymongo.MongoClient(host=host,port=port)
        #
        # # 指向指定的数据库
        # mdb = client[dbname]
        # # 获取数据库里存放数据的表名
        # self.post = mdb[settings['MONGODB_DOCNAME']]
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_DOCNAME"]

        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.sheet = mydb[sheetname]


    # def process_item(self, item, spider):
    #     data = dict(item)
    #     # 向指定的表里添加数据
    #     self.post.insert(data)
    #     return item
    def process_item(self, item, spider):
        data = dict(item)
        self.sheet.insert(data)
        return item

