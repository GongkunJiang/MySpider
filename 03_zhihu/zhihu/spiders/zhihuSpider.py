# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy import Request, FormRequest
from zhihu.items import ZhihuItem


class ZhihuSpider(CrawlSpider):
    name = "zhihuSpider"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/signup?next=%2F"
    ]
    rules = (
        Rule(LinkExtractor(allow=('/question/\d+#.*?',)), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=('/question/\d+',)), callback='parse_page', follow=True),
    )

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-protobuf",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36",
        "Referer": "https://www.zhihu.com/signup?next=%2F"
    }

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://www.zhihu.com/signup?next=%2F", meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        print 'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        # xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        # print xsrf
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,  # "http://www.zhihu.com/login",
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,  # 注意此处的headers
                                          formdata={
                                              '__utma': '',
                                              '__utmc': '',
                                              '__utmz': '',
                                              '_xsrf': '',
                                              '_zap': '',
                                              'capsion_ticket': '',
                                              'd_c0': '',
                                              'q_c1': '',
                                              'tgw_l7_route': '',
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print item['name']
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer'] = problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        return item
