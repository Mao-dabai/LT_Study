# coding:utf-8
'''
@author: 猫大白
Project:
'''

import requests

from lxml import etree


url = "http://newecshop.longtest.cn/admin/index.php?act=menu"
headers = {"Cookie": "ECSCP[admin_id]=13; ECSCP[admin_pass]=26d3cf3d5c5841d97fd867bf01aa7600; real_ipd=221.223.165.196; ECSCP_ID=64d7a5eb4b990f1a96651f9f9ffaece976d3ea25"}

res = requests.get(url,headers = headers)
admin_base_url = "http://newecshop.longtest.cn/admin"
root = etree.HTML(res.text)
elm_list = root.xpath('//li[@class="dropdown"]/ul/li/a')
print("子菜单链接个数",len(elm_list))
menus = []
for link in elm_list:
    href = link.attrib['href']  # 从节点属性字典中取到href属性
    text = link.text   # 获取节点文本，即菜单名
    url = admin_base_url+href
    menus.append([text,url])

for text, url in menus:
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print(text, url, '正常打开')

