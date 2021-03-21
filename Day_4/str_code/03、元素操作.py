# coding:utf-8
'''
@author: 猫大白
Project:元素操作
'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.maximize_window()

# 定位搜索框
# elm = driver.find_element_by_id('kw')
# print(elm.get_attribute('name'))
# elm.send_keys('王冰冰')
# sleep(3)
# elm.clear()
# elm.send_keys('张京'+Keys.ENTER)
# sleep(3)

driver.find_element_by_class_name('soutu-btn').click()
elm = driver.find_element_by_class_name('upload-pic')
elm.send_keys(r'D:\LTTest_Study\Day_4\picture\qq.png')
print('上传按钮是否显示？',elm.is_displayed())

sleep(3)

driver.quit()
