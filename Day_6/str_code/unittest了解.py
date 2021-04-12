# coding:utf-8
'''
@author: 猫大白
Project:Python的unittest框架
'''
from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get('https://www.baidu.com')

#
# driver.find_element('id','kw').send_keys('临渊')
# driver.find_element('id','su').click()
# sleep(0.5)
# assert '临渊' in driver.title
# driver.quit()

# unittest形式
import unittest


class TestBaiDu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element('id','kw').send_keys('临渊')
        self.driver.find_element('id','su').click()
        sleep(0.5)
        assert '临渊' in self.driver.title

