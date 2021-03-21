# coding:utf-8
'''
@author: 猫大白
Project:基础定位方法练习
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')
driver.find_element_by_id('account').send_keys('张三')
driver.find_element_by_id('password').send_keys(123456)

driver.save_screenshot(r'D:\LTTest_Study\Day_4\picture\01.png')