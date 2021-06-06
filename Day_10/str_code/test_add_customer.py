# coding:utf-8
'''
@author: 猫大白
Project:
'''
import csv

import pytest
import requests

username, password = '18010181267', 'HANzhichao@123'

with open('users.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)
    # [
    #     {'customerName': '赵经理', ..},
    #     {'customerName': '赵经理',..},
    # ]


@pytest.fixture(scope='session')
def login():
    url = 'https://www.72crm.com/api/login'
    playload = {"username": username, "password": password}
    res = requests.post(url, json=playload)
    admin_token = res.json()['data']['adminToken']
    return admin_token


@pytest.mark.parametrize('item', data)
def test_add_customer(login, item):
    print('当前数据', item)
    url = 'https://www.72crm.com/api/crmCustomer/add'
    headers = {'Admin-Token': login}
    playload = {
        "entity": item,
        "field": []
    }
    res = requests.post(url, headers=headers, json=playload)
    assert res.status_code == 200, '状态码不为200'
    # assert res.ok  # 200 / 300
    res_dict = res.json()
    assert res_dict['code'] == 0, '响应中的code错误码应为0'
    assert res_dict['data']['customerName'] == item['customerName']
    # todo: 数据库断言
