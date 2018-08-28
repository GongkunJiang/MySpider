# coding=utf-8
import requests
from lxml import etree
import json

url = ('https://www.qiushibaike.com/text/')
response = requests.get(url)
html = etree.HTML(response.text)
result = html.xpath('//div[contains(@class,"article block untagged mb15")]')

n = 1
items = []

for site in result:
    item = {}

    imgurl = site.xpath('./div//img/@src')[0]
    username = site.xpath('./div//h2')[0].text.encode('utf-8').strip()
    content = site.xpath('.//div[@class="content"]/span')[0].text.encode('utf-8').strip()
    vote = site.xpath('./div/span/i')[0].text.encode('utf-8')
    comment = site.xpath('./div/span/a/i')[0].text.encode('utf-8')

    print "No.%d:\n用户头像链接:%s\n用户姓名：%s\n段子内容：%s\n点赞次数：%s\n评论次数：%s" \
          %(n,imgurl,username,content,vote,comment)
    n += 1

    item['imgurl'] = imgurl
    item['username'] = username
    item['content'] = content
    item['vote'] = vote
    item['comment'] = comment

    items.append(item)

    line = json.dumps(items, ensure_ascii=False)
    # output = open('22_qsbk.json', 'w')
    # output.write(line)
    # output.close()
    with open('22_qsbk.json', 'w') as f:
        f.write(line)
