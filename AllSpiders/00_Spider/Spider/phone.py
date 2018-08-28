# -*- coding:utf-8 -*-

import requests
import re

url = 'https://www.zhihu.com/signup?next=%2F'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
data = {
    "phoneNo":"18179043235",
}
html = requests.post(url,data=data,headers=headers)

print html.content