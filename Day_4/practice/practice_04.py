# coding:utf-8
'''
@author: 猫大白
Project:
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.find_element_by_link_text('新闻').click()
print(driver.window_handles[-1])
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
driver.find_element_by_id('ww').send_keys('中美谈判')
driver.find_element_by_class_name('btn').click()
sleep(2)

driver.quit()