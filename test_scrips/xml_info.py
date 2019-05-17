# _*_ coding:utf-8 _*_
from xml.dom import minidom

'''
XML 被设计用来传输和存储数据
HTML被设计用来显示数据
DOM就是针对HTML 和XML 提供的一个API
'''
dom = minidom.parse('C:/Users/ml980245/PycharmProjects/learning/appendix/Class.xml')
# 把整个文档的元素都加载进来，获取文档对象元素
root = dom.documentElement

def Get_Nodeinfo():
    # 根据标签名获取标签对象
    names=root.getElementsByTagName('name')
    ages=root.getElementsByTagName('age')
    citys=root.getElementsByTagName('city')

    print(root.nodeName)
    print(root.nodeValue)
    print(root.nodeType)
    for i in range (4):
        print(names[i].firstChild.data)
        print(ages[i].firstChild.data)
        print(citys[i].firstChild.data)

def Get_NodeAttribute():
    login=root.getElementsByTagName('login')
    for i in range(2):
        username=login[i].getAttribute('username')
        print(username)
        password=login[i].getAttribute('password')
        print(password)

def Get_childNodeInfo():
    tags=root.getElementsByTagName('student')
    print(tags[0].nodeName)
    print(tags[0].nodeType)
    print(tags[0].nodeValue)

Get_Nodeinfo()
Get_NodeAttribute()
Get_childNodeInfo()
