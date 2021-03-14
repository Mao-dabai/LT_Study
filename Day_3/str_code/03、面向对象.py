# coding:utf-8
'''
@author: 猫大白
Project:Python面向对象
'''

class Anianmal(object):
    def eat(self):
        print('吃')
    def run(self):
        print('跑')
#  定义类
class Cat(Anianmal):
    # 初始化
    def __init__(self,name,age):
        # 属性
        # 添加并赋值
        self.name = name
        self.age = age
    # 定义方法
    # def eat(self):
    #     print('猫在喝水。。。。')

    def introduce(self):
        print('%s的年龄是：%d'%(self.name,self.age))

# 创建对象
tom = Cat('汤姆',10)
# 调用
tom.introduce()
tom.eat()

lanmao = Cat('蓝猫',12)
lanmao.introduce()


# 特性
# 多层继承
class Garfield(Cat):
    pass

jfm = Garfield('加菲猫',5)
jfm.introduce()

# 多继承
# class Hello_Kity(Anianmal,Cat):  # Hello_Kity同时继承了Anianmal类和Cat类
#     pass

# 封装
class Send:
    # 私有方法
    # 方法名前加__即将方法变为私有方法
    def __send_msg(self):
        print('正在发送短信')
    # 公共方法
    def send_mag(self,money):
        if money > 100:
            self.__send_msg()
        else:
            print('余额不足，请充值！')

send = Send()
send.send_mag(20)