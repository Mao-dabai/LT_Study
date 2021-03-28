# coding:utf-8
'''
@author: 猫大白
Project:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html#')
driver.maximize_window()

elm = driver.find_element_by_xpath('//input[@value="下拉菜单"]')
action = ActionChains(driver)
action.move_to_element(elm).perform()
driver.find_element_by_xpath('//a[text()="baidu"]').click()
driver.back()
driver.refresh()
sleep(2)
elm_1 = driver.find_element_by_xpath('//button[text()="双击复制文本"]')

# 页面有前进后退动作时，action会失效，需要重新定义
action2 = ActionChains(driver)
action2.double_click(elm_1).perform()
elm_2 = driver.find_element_by_xpath('//button[text()="双击复制文本"]/../input[@id="field1"]')
print(elm_2.get_attribute('value'))

driver.quit()