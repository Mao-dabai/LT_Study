# coding:utf-8
'''
@author: 猫大白
Project:Python的推导式
'''
# 列表推导式
import json

list = [1,23,4,5,6,12,25]

list_a = [i for i in list if i >5]
# print(list_a)


# 字典推导式
dict = {
    'name':'sara','age':12,'sex':'girl'
}

dict_a = {v for k,v in dict.items() if k == 'name'}

# print(dict_a)

list_b = [
    {'name':'sara','age':12,'sex':'girl'},
    {'name':'kevin','age':15,'sex':'boy'},
    {'name':'kitty','age':17,'sex':'girl'}
]

dict_b = {'username' : i['name'] for i in list_b if i['sex'] == 'girl'}

print(dict_b)

for i in list_b:
    if i['sex'] == 'girl':
        print({'username1':i['name']})






for i in range(10):
    print(i)
