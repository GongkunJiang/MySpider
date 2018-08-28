# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# 注意，Python2.x默认编码环境是ASCII，当和取回的数据编码格式不一致时，
# 可能会造成乱码；
# 我们可以指定保存内容的编码格式，一般情况下，我们可以在代码最上方添加：
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# class SinaItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class SinaItem(scrapy.Item):
    # 大类的标题 和 url
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    # 小类的标题 和 子url
    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    # 小类目录存储路径
    subFilename = scrapy.Field()

    # 小类下的子链接
    sonUrls = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()