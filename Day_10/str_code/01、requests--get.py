# coding:utf-8
'''
@author: 猫大白
Project:requests请求
'''
import json

import requests
from pprint import pprint


def get_01():
    response = requests.get("https://httpbin.org/get?name=临渊&age=18")
    # print(response)   # response是一个对象
    #
    # # 反监测，查看对象内有什么方法
    # pprint(response.__dict__)   # 包含属性和属性值
    # pprint(dir(response))  # 仅包含属性

    print("状态码：",response.status_code)
    print("响应文本：",response.text)
    print("响应头：",response.headers)
    print("响应时间：",response.elapsed)


def get_02():
    url = "https://httpbin.org/get"
    url_params = {'name':"临渊",'age':18}
    res = requests.get(url=url,params=url_params)
    print(type(res.text))
    print(repr(res.text))  # 真实格式
    print(res.text)
    res_dict = res.json()  # 把json格式的响应体转换为字典格式
    print(type(res_dict))
    print(res_dict)


def get_03():
    url = "https://www.baidu.com"
    res =requests.get(url)
    try:
        print(res.json())   # 只有当响应文本是json格式时才能正常转字典
    except json.decoder.JSONDecodeError:
        print('响应不是json格式')
        print(res.text)


def get_04():
    url = "https://httpbin.org/get"
    headers = dict(Cookie = 'sessionId=123456;token=abcdefg')
    # headers = {"Cookie" : 'sessionId=123456;token=abcdefg'}
    res = requests.get(url,headers=headers)
    print(res.text)

