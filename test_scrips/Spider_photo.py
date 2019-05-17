# _*_ coding:utf-8 _*_
import urllib
import urllib.request
import re

def load_page(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):
    regx=r'http://[\S]*jpg'
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html))

    num=1
    for img in get_image:
        image=load_page(img)
        with open('D:\\Photo\\%s.jpg' %num, 'wb') as fb:
            fb.write(image)
            print('正在下载第%s张图片' %num)
            num=num+1
    print('下载完成！')

url='http://p.weather.com.cn/2019/05/3189901.shtml#p=1'
html=load_page(url)
get_image(html)
