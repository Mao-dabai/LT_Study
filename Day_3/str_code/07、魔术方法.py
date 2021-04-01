# coding:utf-8
'''
@author: 猫大白
Project:魔术方法和鸭子类型
'''

class B(object):
    def __new__(cls, *args, **kwargs):
        print('创建对象')
        return  super().__new__(cls,*args,**kwargs)

    def __init__(self):
        print('初始化对象')

    def __del__(self):
        print('销毁对象--自动销毁')



b = B()
print(b)

a = 'hello\nkevin\n'

print(str(a))  # str()打印要显示的文本

print(repr(a))  # repr()打印真实文本
