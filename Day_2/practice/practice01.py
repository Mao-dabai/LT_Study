# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 写一个函数完成三次登陆功能，再写一个函数完成注册
# 要求结果如下：
# 三次登陆功能+函数 + 文件操作
# 注册登录的模块
import json


def reg():
    username = input('请输入您注册的用户名：')
    password = input('请输入您注册的密码：')
    user = {'username':username,"password":password}
    user_str = json.dumps(user)
    with open('user.txt','w',encoding='utf-8') as f:
        f.write(user_str)
        f.close()


def login():
    with open('user.txt','r') as f:
        # data = json.loads(f.read())
        data = json.load(f)
        user_name = data.get('username')
        pass_word = data.get('password')

    num = 0
    while num<3:
        a = input('请输入您的用户名：')
        b = input('请输入您的密码：')
        num += 1
        if a == user_name:
            if b == pass_word:
                print('登录成功！！')
                break
            else:
                print('密码错误！！')
                print('您还有%s次机会'%(3-num))
        else:
            print('用户名不存在！！')
            print('您还有%s次机会' % (3 - num))
    else:
        print('三次机会已经用完啦！')

# reg()
login()

