# coding=utf-8
import requests
from lxml import etree

url = ('http://www.qiushibaike.com/8hr/page/1')

try:
    response = requests.get(url)
    resHtml = response.text

    html = etree.HTML(resHtml)
    result = html.xpath('//div[contains(@id,"qiushi_tag")]')
    n = 1
    for site in result:
        item = {}

        imgUrl = site.xpath('./div/a/img/@src')[0].encode('utf-8')
        username = site.xpath('./div/a/@title')[0].encode('utf-8')
        #username = site.xpath('.//h2')[0].text
        content = site.xpath('.//div[@class="content"]/span')[0].text.strip().encode('utf-8')
        # 投票次数
        vote = site.xpath('.//i')[0].text
        #print site.xpath('.//*[@class="number"]')[0].text
        # 评论信息
        comments = site.xpath('.//i')[1].text

        print n,imgUrl, username, content, vote, comments
        n += 1

except Exception, e:
    print e