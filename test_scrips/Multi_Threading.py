# _*_ coding:utf-8 _*_
from time import ctime,sleep
import threading


# define talk and write
def talk(contant,loop):
    for i in range (loop):
        print("Start to talk: %s %s" %(contant,ctime()))
        sleep(2)
def write(contant,loop):
    for i in range (loop):
        print("Start to write: %s %s" %(contant,ctime()))
        sleep(3)

# define and load talk and write thread
threads=[]
t1=threading.Thread(target=talk,args=("Hello 51zxw!",2))
threads.append(t1)

t2=threading.Thread(target=write,args=("Life is short, you need Python!",2))
threads.append(t2)

# execute multi thread
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in  threads:
        t.join()
    print("All Thread end! %s" %ctime())