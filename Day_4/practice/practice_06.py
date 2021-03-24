# coding:utf-8
'''
@author: 猫大白
Project:小米商城UI自动化流程
'''

from selenium import webdriver
from time import  sleep

driver = webdriver.Chrome()
driver.get('https://www.mi.com/')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_class_name('btn-primary').click()
driver.find_element_by_id('username').send_keys('13582105112')
driver.find_element_by_id('pwd').send_keys('xk940819zj')
driver.find_element_by_id('login-button').click()

# driver.find_element_by_id('search').clear()
driver.find_element_by_id('search').send_keys('小米电视')
driver.find_element_by_class_name('search-btn').click()

driver.find_element_by_class_name('goods-list').find_elements_by_class_name('goods-item')[0].click()
driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_link_text('加入购物车').click()
driver.find_element_by_link_text('去购物车结算').click()
driver.find_element_by_link_text('去结算').click()

driver.find_element_by_class_name('address-list').find_elements_by_class_name('address-item')[-1].click()
driver.find_element_by_name('name').send_keys('三爷')
driver.find_element_by_name('telephone').send_keys('12345678901')
driver.find_element_by_name('address').click()
driver.find_element_by_name('search').send_keys('北京市五彩城')
driver.find_element_by_class_name('result-list').find_elements_by_class_name('item-info')[0].find_element_by_link_text('选择').click()
driver.find_element_by_name('addressInfo').send_keys('华润五彩城4层')
driver.find_element_by_class_name('el-dialog__footer').find_elements_by_class_name('btn-primary')[0].click()


