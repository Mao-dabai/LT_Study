# coding:utf-8
'''
@author: 猫大白
Project:requests保持会话
'''
import requests


def session_01():
    s = requests.session()  # 新建会话：1、保持cookie；2、可以配置请求头、授权以及URL参数
    s.headers = {'Cookie':'123456','Token':'abcdef'}  # 给会话设置默认的请求头
    res = s.get('https://httpbin.org/get') # 使用创建的会话发送
    print(res.text)
    res = s.post('https://httpbin.org/post',data={'name':'Kevin'})
    print(res.text)


def session_02():  # 登录状态依赖，cookie、session授权
    # 新建一个会话对象
    s = requests.session()
    # 使用会话对象  请求登录
    url = 'http://newecshop.longtest.cn/admin/privilege.php'
    data = {
        'username': 'test01',
        'password': 'test888',
        'act': 'signin'
    }
    s.post(url,data=data)

    # 使用会话对象，请求其它接口
    res = s.get('http://newecshop.longtest.cn/admin/index.php?act=menu')
    print(res.text)


def session_03():
    # 1. 新建一个会话
    # 2. 请求获取token接口，提取响应中的指定token
    # 3. 把token放到session对应位置中
    # 4. 使用会话请求其他接口
    s = requests.session()
    res = s.get('https://httpbin.org/get')
    token = res.json()['headers']['Host']
    s.headers = {'Token': token}

    res2 = s.post('https://httpbin.org/post',
                        data={'name': 'Kevin'}
                        )
    print(res2.text)


class CRMAPI():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.login()

    def login(self):
        url = 'https://www.72crm.com/api/login'
        playload = {"username": self.username, "password": self.password}
        res = self.session.post(url, json=playload)
        self.session.headers['Admin-Token'] = res.json()['data']['adminToken']  # 提取adminToken放到公共会话到请求头中

    def add_customer(self, name, mobile):
        url = 'https://www.72crm.com/api/crmCustomer/add'
        playload = {
            "entity": {
                "customerName": name,
                "mobile": mobile,
                "telephone": "",
                "website": "",
                "email": "",
                "nextTime": "",
                "remark": "",
                "address": ",,",
                "detailAddress": "",
                "location": "",
                "lng": "",
                "lat": ""
            },
            "field": []
        }
        res = self.session.post(url, json=playload)
        print(res.text)


session_03()