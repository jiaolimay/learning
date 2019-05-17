# _*_ coding:utf-8 _*_
from time import ctime,sleep
import multiprocessing


# define talk and write
def talk(contant,loop):
    for i in range (loop):
        print("Start to talk: %s %s" %(contant,ctime()))
        sleep(2)
def write(contant,loop):
    for i in range (loop):
        print("Start to write: %s %s" %(contant,ctime()))
        sleep(3)

# define and load talk and write process
process=[]
p1=multiprocessing.Process(target=talk,args=("Hello 51zxw!",2))
process.append(p1)

p2=multiprocessing.Process(target=write,args=("Life is short, you need Python!",2))
process.append(p2)

# execute multi thread
if __name__=='__main__':
    for p in process:
        p.start()
    for p in process:
        p.join()
    print("All Process end! %s" %ctime())