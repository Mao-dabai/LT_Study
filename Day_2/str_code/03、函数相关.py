# coding:utf-8
'''
@author: 猫大白
Project:Python的函数
'''

# 函数的定义
# 无参函数
def demo():
    print('1213123123')

# 调用函数
demo()

# 有参函数
def add(x,y):
    if x+y>10:
        print('%d+%d=%d'%(x,y,x+y))
    else:
        print(10)

add(1,10)

# 空函数
def test():
    pass

test()

# return用法
a = int(input('输入第一个数：'))
b = int(input('输入第二个数：'))
def numadd(a,b):

    return '%d+%d=%d'%(a,b,a+b)

numadd(a,b)
print(numadd(a,b))


# 缺省参数
def numadd_1(a,b=33):
    return '%d+%d=%d'%(a,b,a+b)

print('不传入b的实参：',numadd_1(1))  # 不传入b的实参
print('传入b实参：',numadd_1(1,20))  # 传入b的实参

# 动态参数
def numadd_2(a,*args,b=10):
    return a,args,b
print(numadd_2(1,2,3,4))

# 关键字参数
def numadd_3(a,b=10,*args,**kwargs):
    return a,b,args,kwargs

demo = {'name':'zhangsan','age':18}
print(numadd_3(1,2,3,4,5,**demo))