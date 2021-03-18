# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 定义一个类，提供基本属性、方法
# 通过类创建几个不同的对象，打印他们的属性，调用方法


class Person:
    def __init__(self,color,regional,faith):
        self.color = color
        self.regional = regional
        self.faith = faith

    def introduce(self):
        print('%s主要分布在%s，他们信奉%s!!'%(self.color,self.regional,self.faith))

class  Information(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.__init__(self,color='黄种人',regional='北方地区',faith='佛教')
    def basic_inf(self):
        print('%d岁的%s是'%(self.age,self.name),end=''),self.introduce()

Mr_li = Information('李四',28)
Mr_li.basic_inf()