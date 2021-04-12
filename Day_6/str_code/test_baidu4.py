# coding:utf-8
'''
@author: 猫大白
Project:Pytest之数据驱动
'''
from time import sleep
import pytest

DATA = ['张三','李四','临渊','韩志超']

DATA2 = [
    ('临渊','临渊_百度搜索'),
    ('张三','张三_百度搜索'),
    ('李四','李四_百度搜索'),
    ('韩志超','韩志超_百度搜索')
]


@pytest.mark.parametrize('keyword',DATA)
def test_baidu_search1(driver,keyword):
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)

    driver.find_element('id', 'kw').send_keys(keyword)
    driver.find_element('id', 'su').click()
    sleep(1)
    assert keyword in driver.title


@pytest.mark.parametrize('keyword,title',DATA2)    # 拆多个变量，写在一个引号里，用英文逗号隔开
def test_baidu_search2(driver,keyword,title):
    # keyword,title = item[0],item[1]
    # keyword,title = item   # 自动解包
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)

    driver.find_element('id', 'kw').send_keys(keyword)
    driver.find_element('id', 'su').click()
    sleep(1)
    assert title in driver.title