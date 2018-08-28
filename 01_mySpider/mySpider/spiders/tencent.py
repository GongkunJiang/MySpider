# # -*- coding: utf-8 -*-
# import scrapy
# from mySpider.items import TencentItem
# import re
#
# class TencentSpider(scrapy.Spider):
#     name = 'tencent'
#     allowed_domains = ['hr.tencent.com']
#     start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]
#
#     def parse(self, response):
#         for each in response.xpath('//tr[@class="even"]') + response.xpath('//tr[@class="odd"]'):
#             item = TencentItem()
#             item['name'] = each.xpath('./td[1]/a/text()').extract()[0].encode('utf-8')
#             item['detailLink'] = each.xpath('./td[1]/a/@href').extract()[0].encode('utf-8')
#             try:
#                 item['category'] = each.xpath('./td[2]/text()').extract()[0].encode('utf-8')
#             except:
#                 item['category'] = '这个为空'
#             item['peopleNumber'] = each.xpath('./td[3]/text()').extract()[0].encode('utf-8')
#             item['workLocation'] = each.xpath('./td[4]/text()').extract()[0].encode('utf-8')
#             item['publishTime'] = each.xpath('./td[5]/text()').extract()[0].encode('utf-8')
#             yield item
#
#             curnum = int(re.search('(\d+)', response.url).group(1)) + 10
#             nexturl = re.sub('\d+', str(curnum), response.url)
#             yield scrapy.Request(nexturl, callback=self.parse)