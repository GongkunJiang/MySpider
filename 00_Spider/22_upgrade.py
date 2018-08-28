# coding=utf-8
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

url = ('https://www.qiushibaike.com')
response = requests.get(url)
html = BeautifulSoup(response.text,'lxml')
result1 = html.select('div[class="article block untagged mb15 typs_long"]')
result2 = html.select('div[class="article block untagged mb15 typs_hot"]')
result3 = html.select('div[class="article block untagged mb15 typs_old"]')
result4 = html.select('div[class="article block untagged mb15 typs_recent"]')
result = result1 + result2 + result3 + result4

n = 1
items = []
for site in result:
    item = {}
    item['imgurl'] = site.select('div img')[0].attrs['src'] # 贪婪模式
    item['username'] = site.select('div img')[0].attrs['alt'].encode('utf-8')
    item['content'] = site.select('div[class="content"] span')[0].get_text().strip().encode('utf-8')
    item['vote'] = site.select('div span i')[0].get_text().encode('utf-8')
    item['comment'] = site.select('span a i')[0].get_text().encode('utf-8')

    print "No.%d:\n用户头像链接:%s\n用户姓名：%s\n段子内容：%s\n点赞次数：%s\n评论次数：%s" \
          % (n, item['imgurl'], item['username'], item['content'], item['vote'], item['comment'])
    items.append(item)
    n += 1

    line = json.dumps(items, ensure_ascii=False)
    with open('22_qsbk.json','w') as f:
        f.write(line)