# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = (
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#ads",
        "http://www.itcast.cn/channel/teacher.shtml#ago",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#aLinux",
        "http://www.itcast.cn/channel/teacher.shtml#amovies",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apm",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#atest",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#auijp",
        "http://www.itcast.cn/channel/teacher.shtml#aweb",

    )

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')
        for each in teacher_list:
            item = MyspiderItem()
            item['name'] = each.xpath('./h3/text()').extract()[0]
            item['title'] = each.xpath('./h4/text()').extract()[0]
            item['info'] = each.xpath('./p/text()').extract()[0]
            yield item
