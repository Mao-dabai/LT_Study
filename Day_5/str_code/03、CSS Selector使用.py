# coding:utf-8
'''
@author: 猫大白
Project:Python使用CSS Selector
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('input[name=wd]').send_keys('111')
driver.find_element_by_css_selector("input[value=百度一下]").click()

