# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 写一个函数完成三次登陆功能，再写一个函数完成注册
# 要求结果如下：
# 三次登陆功能+函数 + 文件操作
# 注册登录的模块

# 第一种方式
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
# login()


# 第二种方式

def reg_1():
    with open('user_1.txt',mode='w',encoding='utf-8') as f:
        name = input('请输入您要注册的用户名：')
        pwd = input('请输入您的注册密码：')
        f.write('{}\n{}'.format(name,pwd))
        f.close()
        print('注册成功！！！')


def login_1():
    lis = []
    i = 0
    while i<3:
        name = input('请输入您用户名：')
        pwd = input('请输入您的密码：')
        with open('user_1.txt',mode='r',encoding='utf-8') as f:
            for l in f:
                lis.append(l.strip())
        if name == lis[0] and pwd == lis[1]:
            print('登录成功！！！')
            break
        else:
            print('用户名密码错误！！！')
        i+= 1
reg_1()
login_1()