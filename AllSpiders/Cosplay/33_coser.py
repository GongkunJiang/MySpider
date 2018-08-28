# -*- coding:utf-8 -*-
import requests
import urllib2,re
from lxml import etree
from urllib import urlretrieve

class Spider:
    def __init__(self):
        self.url = 'https://bcy.net/item/detail/6593287364309680387'
        self.headers = {"User-Agent" : "Mozilla/5.0"}
    def coserSpider(self):
        req = urllib2.Request(self.url, headers=self.headers)
        html = urllib2.urlopen(req).read()
        selector = etree.HTML(html)
        pattern = re.compile(r'src="(.+?.jpg)/w650')
        links = pattern.findall(html)
        # links = selector.xpath("/html/body/div[@class='div_body']/div[@class='container mt20 _tag-l']/div[@class='row']/div[@class='col-big']/div[@class='_box']/article[@class='post js-item-content']/div[@class='post__content js-content-img-wrap js-fullimg js-maincontent mb0 w650 l-clearfix']/div[@class='content-img-wrap'][8]/div[@class='content-img-wrap-inner']/img[@class='detail_std detail_clickable']/@src")
        for link in links:
            print link
        # content = selector.xpath("//div[contains(@class,'content')]/p/text()")
        # print "".join(content).encode('utf-8')

if __name__ == "__main__":
    # 首先创建爬虫对象
    mySpider = Spider()
    # 调用爬虫对象的方法，开始工作
    mySpider.coserSpider()
