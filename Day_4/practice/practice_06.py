# coding:utf-8
'''
@author: 猫大白
Project:小米商城UI自动化流程
'''

from selenium import webdriver
from time import  sleep
from selenium.webdriver.support.select import Select


# 访问小米商城
driver = webdriver.Chrome()
driver.get('https://www.mi.com/')
driver.maximize_window()
driver.implicitly_wait(30)

# 登录
driver.find_element_by_link_text('登录').click()
try:
    driver.find_element_by_class_name('btn-primary').click()
except Exception:
    print('无同意弹窗')
driver.find_element_by_id('username').send_keys('13582105112')
driver.find_element_by_id('pwd').send_keys('xk940819zj')
driver.find_element_by_id('login-button').click()
sleep(3)
# 搜索小米电视
driver.find_element_by_id('search').send_keys('小米电视')
driver.find_element_by_class_name('search-btn').click()

# 点击第一个商品并加购
driver.find_element_by_class_name('goods-list').find_elements_by_class_name('goods-item')[0].click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_link_text('加入购物车').click()
driver.find_element_by_link_text('去购物车结算').click()
sleep(1)
driver.find_element_by_link_text('去结算').click()

# 添加收货地址
sleep(3)
driver.find_element_by_class_name('address-list').find_elements_by_class_name('address-item')[-1].click()
driver.find_element_by_name('name').send_keys('三爷')
driver.find_element_by_name('telephone').send_keys('13582105112')
driver.find_element_by_name('address').click()
driver.find_element_by_name('search').send_keys('北京 华润五彩城')
sleep(1)
driver.find_element_by_class_name('result-list').find_elements_by_class_name('item-info')[0].find_element_by_link_text('选择').click()
driver.find_element_by_name('addressInfo').send_keys('华润五彩城4层')
driver.find_element_by_class_name('el-dialog__footer').find_elements_by_class_name('btn-primary')[0].click()

driver.find_element_by_link_text('立即下单').click()


driver.find_element_by_link_text('我的订单').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_elements_by_class_name('order-actions')[0].find_element_by_link_text('订单详情').click()
driver.find_element_by_link_text('取消订单').click()
driver.find_element_by_class_name('el-dialog__footer').find_element_by_class_name('btn-primary').click()

driver.quit()


