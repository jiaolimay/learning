# _*_ coding:utf-8 _*_
from time import ctime,sleep

# 说
def talk():
    print("start to talk: %r" %ctime())
    sleep(2)

# 写
def write():
    print("start write %r" %ctime())
    sleep(3)

if __name__=='__main__':
    talk()
    write()
    print("all end ! %r" %ctime())