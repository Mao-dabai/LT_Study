# coding:utf-8
'''
@author: 猫大白
Project:
'''
import csv

import requests

def login():
    # 1. 新建会话
    s = requests.session()
    # 2. 登录
    url = 'http://newecshop.longtest.cn/admin/privilege.php'
    data = {
        'username': 'test01',
        'password': 'test888',
        'act': 'signin'
    }
    s.post(url, data=data)
    return s


def check_menu_page():
    s = login()
    with open('menus.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for text, url in reader:
            res = s.get(url)
            if res.status_code == 200:
                print('检查', text, url, '通过')
            else:
                print('检查', text, url, '不通过')

check_menu_page()



