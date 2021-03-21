# coding:utf-8
'''
@author: 猫大白
Project:浏览器基本操作
'''

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.maximize_window()

# driver.find_element_by_id('kw').send_keys('123213')
driver.find_element('id','kw').send_keys('中美谈判')
driver.find_element('id','su').click()
sleep(3)



driver.quit()
