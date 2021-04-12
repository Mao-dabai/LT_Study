# coding:utf-8
'''
@author: 猫大白
Project:
'''

from selenium import  webdriver
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    driver.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    driver.find_element('name','username').send_keys('test01')
    driver.find_element('name','password').send_keys('test888')
    driver.find_element_by_css_selector('input.button2').click
    sleep(1)
    assert '管理中心' == driver.title