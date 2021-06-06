# coding:utf-8
'''
@author: 猫大白
Project:requests使用数据文件
'''
import csv

with open(r'D:\LTTest_Study\Day_10\files\data.csv',encoding='utf-8') as f:
    # reader = csv.reader(f)  # 返回列表格式数据
    # 第一种跳过第一行标题的方法
    # for row in reader:
    #     if row == ['a','b','c']:
    #         continue
    #     print(row)

    #  第二种跳过第一行标题的方法
    # for index,row in enumerate(reader):
    #     if index == 0:
    #         continue
    #     print(row)

    #  第三种跳过第一行标题的方法
    # header = next(reader)
    # # print(header)
    # for row in reader:
    #     print(row)

    reader2 = csv.DictReader(f)  # 返回字典格式数据
    for row in reader2:
        print(row)