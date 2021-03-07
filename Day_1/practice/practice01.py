# coding:utf-8
'''
@author: 猫大白
Project:第一天学习的作业
'''
"""
用 while 循环实现：
用户登录需求：
1.输入用户名和密码；
2.判断用户名和密码是否正确（name='root',passwd='admin123'）
3.登录仅有三次机会，超过 3 次会报错
4.没有超过三次则登录成功！
"""
# name = 'root'
# passwd = 'admin123'
#
# i = 1
# while i<=3:
#     a = input('请输入用户名：')
#     b = input('请输入密码：')
#     if a == name and b == passwd:
#         print('登录成功！！！')
#         break
#     else:
#         i = i+1
#         print('用户名或密码错误！！！')
#
# else:
#     print('登录仅有三次机会哦！！！')



print('欢迎来到用户登录界面'.center(50,'*'))
trycount = 0
name = 'root'
passwd = 'admin123'
while trycount<3:
    a = input('请输入您的用户名：')
    b = input('请输入您的密码：')
    trycount += 1
    if a == name:
        if b == passwd:
            print('登录成功！！')
            break
        else:
            print('登录失败，密码错误！')
            print('您还有%s次机会'%(3-trycount))
    else:
        print('登录失败，该用户不存在！')
        print('您还有%s次机会'%(3-trycount))
else:
    print('很抱歉，三次机会已经使用完，无法再继续登录！')


