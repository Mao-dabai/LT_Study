# coding:utf-8
'''
@author: 猫大白
Project:Python的Pytest用类实现
'''
from selenium import  webdriver
from time import  sleep
import pytest


class TestBaiDu:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_baidu_search1(self):
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(30)
        print(self.driver.title)

        self.driver.find_element('id', 'kw').send_keys('临渊')
        self.driver.find_element('id', 'su').click()
        sleep(1)
        assert '临渊' in self.driver.title

    def test_baidu_search2(self):
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(30)
        print(self.driver.title)

        self.driver.find_element('id', 'kw').send_keys('韩志超')
        self.driver.find_element('id', 'su').click()
        sleep(1)
        assert '韩志超' in self.driver.title

if __name__ == '__main__':   # 要运行的模块是不是本模块
    pytest.main(['test_baidu2.py::TestBaiDu::test_baidu_search2','-q'])


