# coding:utf-8
'''
@author: 猫大白
Project:Python基础了解
'''
# 注释方法
# print("hello world!")
"""
import  keyword
print(keyword.kwlist)
"""

# 驼峰命名法
userName = '张三'  # 小驼峰命名法
FirstName = '张'   # 大驼峰命名法

# 换行和缩进
print('languages:\tPython')  # \t 表示空四个字符，也成缩进，相当于按一下tab键
print('languages:\npython')  # \n表示换行，相当于按一下enter键
print('languages:\n\tPython')

# 占位符
age = 18
print('my age is %d'%age)
print(f'my age is {age}')
print('my age is {}'.format(age))

# 字符连接 end
print('你是谁？',end='')  # end=''表示以空格连接
print('我是你爸爸')

