# coding:utf-8
'''
@author: 猫大白
Project:
'''

import requests


res = requests.get('https://httpbin.org/get')
host = res.json()['headers']['Host']
headers = {'host':host}

res1 = requests.put(f'https://httpbin.org/put?host={host}',headers=headers)
print(res1.text)
