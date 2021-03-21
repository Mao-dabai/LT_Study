# coding:utf-8
'''
@author: 猫大白
Project:
'''

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')

driver.find_element_by_class_name('dropdown').find_element_by_tag_name('button').click()
sleep(0.5)
driver.find_element_by_class_name('dropdown-menu').find_elements_by_class_name('dropdown-item')[0].click()

driver.quit()