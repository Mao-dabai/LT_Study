# coding:utf-8
'''
@author: 猫大白
Project:iterools的使用
'''
from itertools import groupby

l = ['a','b','a','c','d','c','a','e','f','a','a','b','a','c', 'e']
l.sort()
print(l)

for name, group in groupby(l, key=lambda x:x):
    print(name, len(list(group)))


l2 = [
    {'name': 'Kevin', 'age': 21, 'gender': 'male'},
    {'name': 'Lily', 'age': 12, 'gender': 'female'},
    {'name': 'Eric', 'age': 22, 'gender': 'male'},
    {'name': 'Lucy', 'age': 11, 'gender': 'female'},
]

l2.sort(key=lambda x: x['gender'])
for name, group in groupby(l2, key=lambda x: x['gender']):
    print(name, len(list(group)))
