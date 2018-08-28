# -*- coding=utf-8 -*-

import  urllib  # 负责url编码处理
import urllib2

url = "http://www.baidu.com/s"
world = {"wd":"传智播客"}
world = urllib.urlencode(world) # 转换成url编码格式字符串
newurl = url + "?" + world  # url首个分隔符就是 ？
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",}
request = urllib2.Request(newurl,headers=headers)
response = urllib2.urlopen(request)
print response.read()