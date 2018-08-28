# -*- coding:utf-8 -*-

import requests

proxies = {
    "http": "http://192.168.0.101:9666",
}

response = requests.get("https://www.google.com", proxies = proxies)

print response.url
