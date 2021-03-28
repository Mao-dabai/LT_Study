# coding:utf-8
'''
@author: 猫大白
Project:
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html#')
driver.find_element_by_xpath("//td[text()='王五']/../td[4]/a[text()='查看']").click()