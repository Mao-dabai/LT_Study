# coding:utf-8
'''
@author: 猫大白
Project:Python的四大容器
'''
# list --- 列表

# 列表的定义
l = [1,22,'zhongg']
print(type(l))
# 列表的添加
l.append(666)  # append:追加，给列表的最后面追加一个元素
print('append追加：',l)

l.insert(1,'zzz')  # insert：基于索引在任意位置插入元素
print('insert插入添加：',l)

l.extend('老五') # extend：迭代着追加，在列表的最后面迭代追加一组数据
print('extend迭代追加：',l)

# 列表的删除
r = l.pop(1)  # 通过索引删除列表中对应的元素，该方法返回删除的元素
print('通过pop删除后的结果：',l)
print('pop方法返回删除的元素：',r)

# l.remove('zzz') # 通过元素删除列表中的该元素
# print('remove删除指定元素的结果：',l)

l.clear() # 清空列表
print('clear清空列表',l)

a = [1,'www',22,33]
del a[2]  # 基于索引删除列表中的指定元素
print('del按照索引删除该元素',a)
del a # 删除列表

# 列表的修改
b = [1,'www',22,33,44]
b[0] = '难受' # 基于索引修改元素
print('基于索引改值：',b)

b[1:3] = 'abc'  # 按照切片改值（迭代着增加）
print('按照切片改值：',b)

b[::3] = '对应'  # 按照切片（步长）改值（必须一一对应）
print('按照步长改值：',b)

# 列表的查询
print('a' in b)

# 列表的排序
b1 = [1,3,2,5,4]
b1.sort()
print('从小到大排序：',b1)
b1.sort(reverse=True)
print('从大到小排序：',b1)


# tuple --- 元组

# 元组的定义
a1 = (1,) # 一个元素定义需要加逗号
print(type(a1))
a2 = (1,2,3)

# 元组本身是不可以修改的，但是可以嵌套修改
a3 = (1,2,2,['a','b','c'])
a3[3][1] = 'B'  # 嵌套修改
print('嵌套修改后的结果：',a3)

# 元组的查找
print(a3.index(2))  # 基于元素查元组中该元素的索引
print(a3.count(2))  # 查询元素在元组中出现的次数

# 字典和集合

# 字典的定义
infor = {'name':"张三"}
print(type(infor))

# 字典的添加
infor['age'] = 16
print('字典添加后的结果：',infor)

# 字典的修改
infor['age'] = 18
print('字典修改后的结果：',infor)

# 字典的删除
del infor['age']  # 基于key删除键值对

# 字典的查询
print(infor.get('name')) # 基于key查询对应的value

# 取字典所有键
dict1 = {'name': '张三', 'age': 18}
print('字典中所有的键：',dict1.keys())
print('字典中所有的值：',dict1.values())

# set --- 集合 拥有自动去重功能

# 集合的定义
s = {1,2,3,4}
print(type(s))

# 集合的添加
s.add('Python')  # add：添加元素，默认最后一位
print('通过add添加集合为：',s)

# 集合的删除
s.remove(1)  # 删除一个元素
print('通过remove删除后集合为：',s)

s.pop()  # 随机删除一个元素
print('通过pop随机删除一个元素，集合为：',s)

s.clear()  # 清空集合
print(s)
