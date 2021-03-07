# coding:utf-8
'''
@author: 猫大白
Project:Python之文件操作
'''

# 写文件
# f = open('test.txt','w')
# f.write('Hello,大家好')
# f.close()

# 读文件
# f = open(r'C:\Users\Administrator\Desktop\新建文本文档.txt',mode='r')
# data = f.read()  # 读文件，若文件编码不是ANSI可能会报错
# print(data)
# f.close

# 追加文件
# f = open(r'C:\Users\Administrator\Desktop\新建文本文档.txt',mode='a')
# f.write('我试谁啊加上哈法')
# f.close()
# f = open(r'C:\Users\Administrator\Desktop\新建文本文档.txt',mode='r')
# data = f.read()
# print(data)
# f.close()

# # 读取几个字
# data = f.read(3)  # 3限制几个字，默认全部
# print(data)

# data = f.readline()   # 默认读取一行
# print('readline默认读取一行:',data)

# data = f.readlines()  # 返回一个列表，读取全部
# print('readlines返回一个列表，读取全部：',data)

# 另一种打开文件方式
with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt',mode='r') as f:
    data = f.read()
    print(data)
    f.close()