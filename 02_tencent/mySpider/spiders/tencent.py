# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mySpider.items import TencentItem


class TencentSpider(CrawlSpider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    page_lx = LinkExtractor(allow=("start=\d+"))

    rules = [
        Rule(page_lx, callback="parseContent", follow=True)
    ]

    def parseContent(self, response):
        for each in response.xpath('//tr[@class="even"]') + response.xpath('//tr[@class="odd"]'):
            item = TencentItem()
            item['name'] = each.xpath('./td[1]/a/text()').extract()[0].encode('utf-8')
            item['detailLink'] = each.xpath('./td[1]/a/@href').extract()[0].encode('utf-8')
            try:
                item['category'] = each.xpath('./td[2]/text()').extract()[0].encode('utf-8')
            except:
                item['category'] = ''
            item['peopleNumber'] = each.xpath('./td[3]/text()').extract()[0].encode('utf-8')
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0].encode('utf-8')
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0].encode('utf-8')
            yield item
