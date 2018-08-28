# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = scrapy.Field()
#     title = scrapy.Field()
#     info = scrapy.Field()


class TencentItem(Item):
    name = Field()
    detailLink = Field()
    category = Field()
    peopleNumber = Field()
    workLocation = Field()
    publishTime = Field()

# class ZhihuItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     url = Field()  #保存抓取问题的url
#     title = Field()  #抓取问题的标题
#     description = Field()  #抓取问题的描述
#     answer = Field()  #抓取问题的答案
#     name = Field()  #个人用户的名称
