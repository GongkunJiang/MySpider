#coding:utf-8
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
           'Cookie': 'da_a=77206194', 'Referer': 'http://www.demlution.com/'}
# data =
# print data
r = requests.post('http://account.xici.net/valid/sendcodephone/phone_number::::http://passport.hupu.com/register', headers=headers)

print(r.text)