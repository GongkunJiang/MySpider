# coding=utf-8
import json
import chardet

# strDict = '{"city": "北京", "name": "大猫"}'
#
# listStr = [1, 2, 3, 4]
# tupleStr = (1, 2, 3, 4)
# dictStr = {"city": "北京", "name": "大猫"}
#
# print chardet.detect(json.dumps(dictStr, ensure_ascii=False))

# listStr = [{"city": "北京"}, {"name": "大刘"}]
# json.dump(listStr, open("20_json_listStr.json","w"), ensure_ascii=False)
#
# dictStr = {"city": "北京", "name": "大刘"}
# json.dump(dictStr, open("20_json_dictStr.json","w"), ensure_ascii=False)

strList = json.load(open("20_json_listStr.json"))
print strList

strDict = json.load(open("20_json_dictStr.json"))
print strDict
