# coding:utf-8
'''
@author: 猫大白
Project:Python的Pytest组成
'''
from selenium import  webdriver
from time import  sleep


def setup_function():
    global driver
    driver = webdriver.Chrome()


def teardown_function():
    driver.quit()


def test_baidu_search1():

    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    print(driver.title)

    driver.find_element('id', 'kw').send_keys('临渊')
    driver.find_element('id', 'su').click()
    sleep(1)
    assert '临渊' in driver.title


def test_baidu_search2():

    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    print(driver.title)

    driver.find_element('id', 'kw').send_keys('韩志超')
    driver.find_element('id', 'su').click()
    sleep(1)
    assert '韩志超' in driver.title

