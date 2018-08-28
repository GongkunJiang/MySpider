# -*- coding:utf-8 -*-

# import requests
#
# # 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
# proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }
#
# response = requests.get("https://www.baidu.com", proxies = proxy)
#
# print response.text


# import requests
#
# auth=('test', '123456')
#
# response = requests.get('https://192.168.199.107', auth = auth)
#
# print response.text

import requests
response = requests.get("https://www.baidu.com/", verify=True)

# 也可以省略不写
# response = requests.get("https://www.baidu.com/")
print response.content