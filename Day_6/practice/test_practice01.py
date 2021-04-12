# coding:utf-8
'''
@author: 猫大白
Project:
'''
from time import sleep
from selenium import webdriver
import pytest


DATA3 = [
    ('test01', 'test888'),
    ('admin', 'admin888'),
    ('abc', 'abc888')
]


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('username,password',DATA3)
def test_login(driver,username,password):
    driver.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    driver.find_element('name','username').send_keys(username)
    driver.find_element('name','password').send_keys(password)
    driver.find_element('class name', 'button2').click()
    sleep(1)
    assert '管理中心' == driver.title