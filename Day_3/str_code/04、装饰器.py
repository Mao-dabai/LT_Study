# coding:utf-8
'''
@author: 猫大白
Project:Python的装饰器相关
'''

# 基础装饰器

def deco1(func):
    print('装饰器func')  # 在函数执行前增加一个处理过程
    return func

# 处理函数参数
def deco2(func):
    def new_func(a,b):
        if isinstance(a,int) and isinstance(b,int):
            return func(a,b)
        else:
            print('参数格式错误')
    return new_func

# 带参数的装饰器
def deco3(check=True):
    def deco2(func):   # 真正的装饰器
        def new_func(a, b):
            if isinstance(a, int) and isinstance(b, int):
                return func(a, b)
            else:
                print('参数格式错误')
        if check is True:
            return new_func
        return func

    return deco2

@deco3()
def add(a:int,b:int):
    print(a+b)
    return a+b

add(1,"2")


# TODO 闭包
