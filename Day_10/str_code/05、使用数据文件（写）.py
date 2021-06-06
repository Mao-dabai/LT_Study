# coding:utf-8
'''
@author: 猫大白
Project:
'''
import csv

import requests
from lxml import etree

# 1. 新建会话
s = requests.session()

# 2. 登录
url = 'http://newecshop.longtest.cn/admin/privilege.php'
data = {
    'username': 'test01',
    'password': 'test888',
    'act': 'signin'
}
res = s.post(url, data=data)

# 3. 请求菜单页面，拿到html
res = s.get('http://newecshop.longtest.cn/admin/index.php?act=menu')
print(res.text)

# 4. 解析html，拿到所有的菜单和连接
root = etree.HTML(res.text)
elm_list = root.xpath('//li[@class="dropdown"]/ul/li/a')
menus = []
for link in elm_list:
    text = link.text  # 获取节点文本---即菜单名
    url = 'http://newecshop.longtest.cn/admin/' + link.attrib['href']   # 从节点属性字典中获取到href属性
    menus.append([text, url])

# 5. 写入csv文件
header = ['text', 'url']
with open(r'D:\LTTest_Study\Day_10\files\menus.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(menus)
