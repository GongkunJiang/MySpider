# -*- coding: utf-8 -*-
import scrapy,requests
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider
from Cosplay.items import CoserItem
from lxml import etree

class CoserSpider(scrapy.Spider):
    name = "coser2"
    allowed_domains = ["bcy.net"]
    start_urls = [
        'https://bcy.net/coser'
    ]

    def parse(self, response):
        links = response.xpath("//li[@class='js-smallCards _box']/a/@href").extract()
        i = 1
        for link in links:
            link = 'https://bcy.net%s' % link
            # print 'No.%d\t'% i + link
            i += 1
            request = scrapy.Request(link, callback=self.parse_item)
            yield request

    def parse_item(self, response):

        item = CoserItem()
        item['name'] = response.xpath("//div[@class='mb10 dib']/a/text()").extract()
        item['info'] = response.xpath("//div/p[@class='mb20']/text()").extract()
        item['url'] = response.url
        html = BeautifulSoup((requests.get(response.url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"})).text, 'lxml')
        image_urls = html.select("div[class='content-img-wrap-inner'] img")
        # print item['name']
        # print item['info']
        # print item['url']
        for url in image_urls:
            print url
        # l = ItemLoader(item=CoserItem(), response=response)
        # l.add_xpath('name', "//div[@class='mb10 dib']/a/text()")
        # l.add_xpath('info', "//div/p[@class='mb20']/text()")
        # #l.add_xpath('image_urls',"//div[@class='content-img-wrap-inner']/img[@src]")
        # l.add_value('url', response.url)
        # # //div[@class='content-img-wrap']//img/@src
        # # 抓不到
        # urls = l.get_xpath("//div[@class='content-img-wrap']//img/@src")
        # # urls = [url.replace('/w650', '') for url in urls]
        # l.add_value('image_urls', urls)
        # # l.add_xpath('image_urls',"//div/p[@class='mb20']/text()")
        # yield l.load_item()