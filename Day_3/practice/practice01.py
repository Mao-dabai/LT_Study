# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 定义一个类，提供基本属性、方法
# 通过类创建几个不同的对象，打印他们的属性，调用方法


class Car():
    def __init__(self, color, mali, mode):
        self.color = color
        self.mali = mali
        self.mode = mode


    def move(self):
        print('%s的%s以%d马力的速度在飞速行驶'% (self.color,self.mode,self.mali))

BMW_X9 = Car('红色', 200,'宝马X9')
BMW_X9.move()

list = [1,2,3,45,6]
print(list[10:])
