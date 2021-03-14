# coding:utf-8
'''
@author: 猫大白
Project:Python的异常处理
'''
# print(num)  # NameError
# 11/0  # ZeroDivisionError
# open('232.txt')  # FileNotFoundError


# 处理异常
try:
    print(num)
except NameError:
    print('捕获异常！！')

# 多个异常处理
try:
    print(num)
    11/0
except (NameError,ZeroDivisionError):
    print('捕获异常1！！')

# 万能异常处理
try:
    print(num)
    11/0
except Exception as a:
    print(a)  # 只打印第一个错误
    print('捕获异常2！！！')