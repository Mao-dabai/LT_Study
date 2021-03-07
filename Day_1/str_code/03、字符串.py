# coding:utf-8
'''
@author: 猫大白
Project:Python字符串学习
'''
# 字符串命名
a = 'demo'
b = str('demo')
print(type(a))
print(type(b))
print('--------------------------------------------------------')

# 字符串的索引
A = 'demo'
print('打印d：',A[0])  # 0是索引
print('打印d和e：',A[:2])  # [:2]从0开始截取索引为0和1的值
print('打印o：',A[-1])  # -1倒序截取最后一个
print('--------------------------------------------------------')

# 字符串的查找
A1 = 'Hello world!!'
print('o在A1中有%d个'%A1.count('o'))  # count:查找字符串中特定字母的出现次数
print('o在A1的索引为：',A1.index('o')) # index:返回从左第一个指定字符的索引，找不到报错
print('h在A1中的索引为：',A1.find('h')) # find:返回从左第一个指定字符的索引，找不到返回-1
print('--------------------------------------------------------')

# 字符串的分割
mystr = "hello world java\n welecome to \nbeijing"
print(mystr.splitlines())  # splitlines:按照行分隔，返回一个包含各行作为元素的列表,按照换行符分割
print(mystr.split('o'))  # split('o')：按照特定字母分割，返回一个不包含o且在o处切割的各个元素列表
print('--------------------------------------------------------')

# 字符串的替换
A2 = 'hello world'
print(A2.replace('o','a'))  # 从左到右替换o为a
print(A2.replace('o','a',1)) # 从左到右替换第1个o为a；1表示替换一个
print('--------------------------------------------------------')

# 字符串的修饰
str = " Love "
print(str.center(50,"*")) # 让字符串在指定的长度居中
print(str.ljust(30,"*")) # 让字符串在指定的长度左齐
print(str.rjust(30,"*")) # 让字符串在指定的长度右齐
print(str.rstrip()) # 默认去除右边的空格
print(str.lstrip()) # 默认去除左边的空格
print(str.strip()) # 默认去除两边的空格
# format 按照顺序，将后面的参数传递给前面的大括号
python = '{} love {}'
print(python.format('I','you'))
print('--------------------------------------------------------')

# 字符串的变形
print('hello'.upper()) # upper()：将字符串中所有小写字母转换为大写
print('HELLO'.lower()) # lower()：将字符串中所有大写字母转换为小写
print('HelLo'.swapcase()) # swapcase()：将字符中所有的字母大小写互换
print('hello world ok'.title()) # title()：将字符中的单词首字母大写
print('hello world'.capitalize())  # capitalize()：将字符串首字母大写
print('--------------------------------------------------------')

# 字符串的判断
print("123456e".isalnum()) # isalnum：判断字符串是否完全由字母或数字组成
print("123456".isdigit()) # isdigit：判断字符串是否完全由数字组成
print("HELLO".isupper()) # isupper：判断字符串当中的字母是否完全是大写
print("hello".islower()) # islower：判断字符串当中的字母是否完全是小写
print("Hello world".istitle()) # istitle：判断字符串的开头首字母是否大写
print("HelloWorld".isalpha()) # isalpha：判断字符串是否完全由字母组成

print("hello world 2.txt".startswith("hello")) # startwith：判断字符串的开头
print("hello world 2.txt".endswith(".txt")) # endswith：判断字符串是否.txt 结尾


print("hello world".split(" ")) # split()：按照空格切 ，结果变成列表的元素
s2= "testlaoweeubaisheng "
print(s2.split('e',2)) # 2为设置分隔次数
s = "test laowu baisheng "
print(s.split()) # 默认按照空格分隔
s1 = "test laowu ， baisheng "
print(s1.split('，')) # 按照，号分隔。
