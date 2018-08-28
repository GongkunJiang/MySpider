# -*- coding: utf-8 -*-
import scrapy
# 只要是需要提供post数据的，就可以用这种方法。下面示例里post的数据是账户密码：
# 到头来还要传更多的参数（从Fiddler获取）
# 原来这就是方法3呀
class Renren1Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
                url = url,
                formdata = {
                    "email": "18179043235",
                    "icode": "origURL http://www.renren.com/home",
                    "domain": "renren.com",
                    "key_id": "1",
                    "captcha_type": "web_login",
                    "password": "3648c86b4ba5b266b0e116801fee8f32f9a86a1bab891b29b3adc5c721f672bd",
                    "rkey": "cb15f985754fd884a44506ff5db1256e",
                    "f": "http%3A%2F%2Fwww.renren.com%2F967772796",
                },
                callback = self.parse_page)

    def parse_page(self, response):
        with open("../login1.html", "w") as filename:
            filename.write(response.body)
