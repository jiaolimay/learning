# _*_ coding:utf-8 _*_
def fun_args1(args):
    print('args is %s' %args)

def fun_args2(args1,args2):
    print('args1 is %s args2 is %s' %(args1,args2))

def fun_var_args(*args):
    for value in args:
        print('args : ', value)

# fun_args2('51zxw','selenium')

fun_var_args('51zuw','python')