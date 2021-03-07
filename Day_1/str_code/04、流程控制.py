# coding:utf-8
'''
@author: 猫大白
Project:Python的流程控制
'''
"""
程序执行的三种方式：顺序执行、选择执行、循环执行

"""

# if判断
# # 判断是否白富美？
# color = input('你白吗？')
# money = input('请输入您的财产总和：')
# beautiful = input('你美吗？')
#
# if color == '白' and money>1000000 and beautiful == '美':
#     print('您真是一个白富美！！！！')
# else:
#     print('屌丝一个.......')
#
# # 根据成绩判断登记
# score = float(input('请输入您的考试分数：'))
# if score>=90 and score<=100:
#     print('本次考试，等级为A')
# elif score>=80 and score<90:
#     print('本次考试，等级为B')
# elif score>=70 and score<80:
#     print('本次考试，等级为C')
# elif score>=60 and score<70:
#     print('本次考试，等级为D')
# elif score>=0 and score<60:
#     print('本次考试，等级为E')
# else:
#     print('请输入1~100之间的数')

# while循环
# while循环入门
# num = 1
# while num<=10:
#     num+=1

# 计算1~100的累计和
# i = 1
# sum = 0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# 打印矩形
# i = 1
# while i<5:
#     print('******')
#     i+=1

# 九九乘法表
# i = 1
# while i<10:
#     j=1
#     while j<i:
#         print('%d*%d=%d\t'%(j,i,j*i),end='')
#         j+=1
#     print('')  # 为了换行显示
#     i+=1

# for循环
# for循环的遍历
# name = 'python'
# for x in name:
#     # print(x,'_____')
#     if x == 't':
#         continue
#     print(x)


# 嵌套使用
# 如果有敏感词的话就题把敏感词替换成*****并且赶紧退出，没有敏感词的话可以继续输入
while True:
    name=input('请输入内容：')
    if"敏感词"in name or "政治话题"in name:
        v = name.replace('敏感词','*****')
        v1 = v.replace('政治话题','*****')
        print(v1)
        exit()
    else:
        print(name)