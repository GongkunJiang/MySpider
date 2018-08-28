# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import scrapy,re,urllib2
from scrapy.contrib.loader import ItemLoader
from Cosplay.items import CoserItem


class CoserSpider(scrapy.Spider):
    name = "coser"
    allowed_domains = ["bcy.net"]
    start_urls = [
        'https://bcy.net/coser',
        'https://bcy.net/circle/timeline/showtag?since=25897.569&grid_type=flow&sort=hot&tag_id=399',
        'https://bcy.net/circle/timeline/showtag?since=25897.527&grid_type=flow&sort=hot&tag_id=399',
        'https://bcy.net/circle/timeline/showtag?since=25897.492&grid_type=flow&sort=hot&tag_id=399',
        'https://bcy.net/circle/timeline/showtag?since=25897.425&grid_type=flow&sort=hot&tag_id=399',
    ]

    def parse(self, response):
        sel = Selector(response)
        # //li[contains(@data-since,'25893')]/a/@href
        # //li[@class='js-smallCards _box']/a/@href
        for link in sel.xpath("//li[@class='js-smallCards _box']/a/@href").extract():
            link = 'https://bcy.net%s' % link
            request = scrapy.Request(link, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        l = ItemLoader(item=CoserItem(), response=response)
        l.add_xpath('name', "//div[@class='mb10 dib']/a/text()")
        l.add_xpath('info', "//div/p[@class='mb20']/text()")
        #l.add_xpath('image_urls',"//div[@class='content-img-wrap-inner']/img[@src]")
        l.add_value('url', response.url)
        # //div[@class='content-img-wrap']//img/@src
        # 抓不到,终于试出来了 可以用正则爬
        html = urllib2.urlopen(urllib2.Request(response.url,headers={"User-Agent" : "Mozilla/5.0"})).read()
        urls = re.compile(r'src="(.+?.jpg)/w650').findall(html)
        # urls = l.get_xpath("//div[@class='content-img-wrap']//img/@src")
        # urls = [url.replace('/w650', '') for url in urls]
        l.add_value('image_urls', urls)
        # l.add_xpath('image_urls',"//div/p[@class='mb20']/text()")
        yield l.load_item()