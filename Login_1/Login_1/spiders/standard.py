# -*- coding: utf-8 -*-
import scrapy
# 正统模拟登录方法：
# 首先发送登录页面的get请求，获取到页面里的登录必须的参数（比如说zhihu登陆界面的 _xsrf）
# 然后和账户密码一起post到服务器，登录成功

#！！！真神奇，出了账号密吗啥都不需要！


class Renren2Spider(scrapy.Spider):
    name = "renren2"
    allowed_domains = ["renren.com"]
    start_urls = (
        "http://www.renren.com/PLogin.do",
    )

    # 处理start_urls里的登录url的响应内容，提取登陆需要的参数（如果需要的话)
    def parse(self, response):
        # 提取登陆需要的参数
        #_xsrf = response.xpath("//_xsrf").extract()[0]

        # 发送请求参数，并调用指定回调函数处理
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {"email" : "15079050278", "password" : "050278"},#, "_xsrf" = _xsrf},
                callback = self.parse_page
            )

    # 获取登录成功状态，访问需要登录后才能访问的页面
    def parse_page(self, response):
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    # 处理响应内容
    def parse_newpage(self, response):
        with open("../login2.html", "w") as filename:
            filename.write(response.body)