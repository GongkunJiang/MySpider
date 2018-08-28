# -*- coding=utf-8 -*-

import urllib2
import random

url = "http://www.itcast.cn"

# ua_list = [
#     "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
#     "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
#     "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS... "
# ]
# user_agent = random.choice(ua_list)
# request = urllib2.Request(url)
# request.add_header("User-Agent", user_agent)
# request.get_header("User-agent")
# IE 9.0 的 User-Agent, 包含在 ua_header里
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",}
request = urllib2.Request(url, headers=headers)
# 也可以通过调用Request.add_header()添加/修改一个特定的header
request.add_header("Connection","keep-alive")

# 也可以通过调用request.get_header()来查看header信息
# request.get_header(header_name="Connection")

response = urllib2.urlopen(request)

# print response.code     # 可以查看相应代码
html = response.read()

print html