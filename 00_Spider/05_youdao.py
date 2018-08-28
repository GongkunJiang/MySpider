# -*- coding=utf-8 -*-
import urllib
import urllib2

# POST请求的目标URL
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# 完整的headers
headers = {
    "Host": "fanyi.youdao.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://fanyi.youdao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://fanyi.youdao.com/",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Content-Length": "226"
    }

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "	AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1534860277899",
    "sign": "0b4d320c446ece4a389154ba35cc23c7",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false",
}
# 经过urlencode转码
data = urllib.urlencode(formdata)
# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)
print response.read()