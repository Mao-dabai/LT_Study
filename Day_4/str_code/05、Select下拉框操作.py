# coding:utf-8
'''
@author: 猫大白
Project:Select下拉框
'''
from time import sleep

from selenium   import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')
# 定位select元素
area = driver.find_element_by_id('area')
# 传入select元素，创建select对象
s = Select(area)
# 用index/value或显示文字选择
s.select_by_visible_text('北京')
sleep(1)
s.select_by_visible_text('上海')
sleep(1)
s.select_by_visible_text('河北')