# coding:utf-8
'''
@author: 猫大白
Project:对话框和新窗口处理
'''

from time import sleep
from selenium   import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')
driver.get('file:///C:/Users/admin/Desktop/selenium_demo/selenium_demo/selenium.html')

# 模态框/div弹窗/dom弹窗 -- 直接定位元素
# TODO
driver.find_elements_by_class_name('card')[4].find_element_by_class_name('btn').click()
sleep(2)
driver.find_element_by_class_name('modal-footer').find_element_by_class_name('btn').click()

# alert弹窗 -- switch_to.alert
import time
A = driver.find_element_by_class_name('container').find_element_by_id('alert')

a = str(time.time())

# 新窗口  -- switch_to.window(new_window_handel)



# 框架切换  -- switch_to.frame()