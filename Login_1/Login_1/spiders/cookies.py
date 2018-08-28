# -*- coding: utf-8 -*-
import scrapy
# 直接使用保存登陆状态的Cookie模拟登陆
# 如果实在没办法了，可以用这种方法模拟登录，虽然麻烦一点，但是成功率100%
class RenrenSpider(scrapy.Spider):
    name = "renren3"
    allowed_domains = ["renren.com"]
    start_urls = (
        'http://www.renren.com/324925435',
    )

    cookies = {
        "anonymid": "jlc700pg-jacgj9;",
        "depovince": "JX;",
        "_r01_": "1;",
        "ick_login": "afea2073-8e9d-46ee-a9cd-c7a17eef4789;",
        "JSESSIONID": "abcMtT4WRJFE24TeMh7vw;",
        "ick": "5ef49b90-3e6d-481f-a5af-fbd0544eac8d;",
        "__utma": "151146938.897796537.1535369057.1535369057.1535369057.1;",
        "__utmc": "151146938;",
        "__utmz": "151146938.1535369057.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do;",
        "XNESSESSIONID": "e7db85db0f3b;", " first_login_flag": "1;",
        "_ga": "GA1.2.897796537.1535369057;",
        "_gid": "GA1.2.2035663705.1535371082;",
        "wp_fold": "0;", " ln_uact": "18990887912;",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn121/20150529/1110/h_main_JDsM_806d0000b0ef1986.jpg;",
        "jebecookies": "71f22958-5cf8-421f-a96f-0b65c22a1a22|||||;",
        "_de": "A5782E290232B4862175E3B7C0A76F2F;",
        "p": "38f2ff64c0366caef302c728138a123e0;",
        "t": "38edab733e08af156e02f5c103c2ca670;",
        "societyguester": "38edab733e08af156e02f5c103c2ca670;",
        "id": "555342830;",
        "xnsid": "848ac02f;",
        "ver": "7.0;",
        "loginfrom": "null;",

    }

    # 可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies = self.cookies, callback = self.parse_page)

    # 处理响应内容
    def parse_page(self, response):
        print "===========" + response.url
        with open("../login3.html", "w") as filename:
            filename.write(response.body)