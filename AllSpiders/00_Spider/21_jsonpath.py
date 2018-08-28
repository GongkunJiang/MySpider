# coding=utf-8
import jsonpath
import json
import chardet
import requests

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = requests.get(url)
html = response.text

# 把json格式字符串转换成python对象
json_obj = json.loads(html)

# 从根节点开始，匹配name节点
city_list = jsonpath.jsonpath(json_obj,'$..name')
print city_list
print type(city_list)
content = json.dumps(city_list, ensure_ascii=False)
print content

with open('21_jsonpath_city.json','w') as f:
    f.write(content.encode('utf-8'))