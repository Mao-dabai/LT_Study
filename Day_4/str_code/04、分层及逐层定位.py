# coding:utf-8
'''
@author: 猫大白
Project:分层及逐层定位
'''

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')
elm_list = driver.find_elements_by_name('gender')
print('女是否选中？',elm_list[-1].is_selected())
