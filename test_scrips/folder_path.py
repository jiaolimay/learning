# _*_ coding:utf_8 -*_
import os
import csv

'''
path='C:\\Users\\ml980245\\PycharmProjects\\learning\\test_scrips\\By.py'
print(path)
print(os.getcwd()+'\\'+'By.py')
print(os.getcwd()[:-6])
print(os.getcwd()[0:3])
print(os.listdir('C:\\Users\\ml980245\\PycharmProjects\\learning\\test_scrips')[1])
'''

# path='C:\\Users\\ml980245\\PycharmProjects\\1.txt'
# f=open(path,'r')
'''	
file.read([size])从文件读取指定的字节数，如果未给定或为负则读取所有
'''
# print(f.read())
# print(f.readline())
# print(f.readlines()[1])

'''文件操作写'''
# f=open('C:\\Users\\ml980245\\PycharmProjects\\tt.txt','w')
# f.write('1test')
# f.write('测试')
# s=['\na\n','b\n','c']
# f.writelines(s)
# f.close()

'''csv操作读'''
# pathcsv='D:\\jmeter\\apache-jmeter-5.0\\bin\\examples\\CSVSample_user.csv'
# csvfile=csv.reader(open(pathcsv,'r'))
# '''['u1', 'p1']
#    ['u2', 'p2']'''
# for line in csvfile:
#     '''第几列'''
#     print(line[0])

'''csv操作写'''
pathcsvw=os.getcwd()+'\\'+'test.csv'
print(pathcsvw)
f=open(pathcsvw,'w')
w=csv.writer(f)
dic={'测试':1,'软件':2,'工具':3}
for key in dic:
    w.writerow([key,dic[key]])
f.close()