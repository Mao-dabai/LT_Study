# coding:utf-8
'''
@author: 猫大白
Project:Pytest的fixture使用
'''

from selenium import  webdriver
from time import  sleep
import pytest


@pytest.fixture(scope='function',autouse=True)
def driver():
    print('setup')
    driver = webdriver.Chrome()
    yield  driver
    print('teardown')
    driver.quit()


# @pytest.mark.usefixtures("start_quit")
def test_baidu_search1(driver):
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    print(driver.title)

    driver.find_element('id', 'kw').send_keys('临渊')
    driver.find_element('id', 'su').click()
    sleep(1)
    assert '临渊' in driver.title


def test_baidu_search2(driver):
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    print(driver.title)

    driver.find_element('id', 'kw').send_keys('韩志超')
    driver.find_element('id', 'su').click()
    sleep(1)
    assert '韩志超' in driver.title
