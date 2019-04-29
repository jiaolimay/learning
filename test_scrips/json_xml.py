# -*- coding:utf-8 -*-
import json
import xml.dom.minidom

'''字典'''
test1={'android':'appium','web':'selenium','interface':'requests'}

'''将 Python 对象编码成 JSON 字符串'''
js=json.dumps(test1)
# print(js)

# '''将已编码的 JSON 字符串解码为 Python 对象'''
# print(json.loads(js))
# '''<class 'dict'>'''
# print(type(json.loads(js)))

# '''写json'''
# f1=open('D:\\test.json','w')
# json.dump(js,f1)

'''读json'''
f2=open('D:\\test.json','r')
print(json.load(f2))


