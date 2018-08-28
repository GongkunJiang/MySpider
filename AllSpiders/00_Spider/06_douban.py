# -*- coding:utf-8 -*-
import urllib
import urllib2
url = "https://movie.douban.com/j/chart/top_list?type=20&interval_id=100%3A90&action="
headers={"User-Agent": "Mozilla...."}

# 处理所有参数
formdata = {
    'start':'0',
    'limit':'20'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)

print response.read()