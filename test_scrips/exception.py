# _*_ coding:utf_8 -*_
'''
try:
    stu = 'Jack'
    print(stu)
except BaseException as msg:
    print(msg)
else:
    print('stu is defined ！')

try:
    # stu = 'Jack'
    print(stu)
except BaseException as msg:
    print(msg)
else:
    print('stu is defined ！')
finally:
    print('The end ！')
'''

def division(x,y):
    if(y==0):
        ''':raise只能用于python标准异常类'''
        raise ZeroDivisionError('Zero is not allowed!')
    return x/y

try:
    division(8,0)
except BaseException as msg:
    print(msg)
