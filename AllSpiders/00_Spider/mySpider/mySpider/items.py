# -*- coding: utf-8 -*-

import scrapy


class ItcastItem(scrapy.Item):
    # 姓名
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 个人简介
    info = scrapy.Field()
