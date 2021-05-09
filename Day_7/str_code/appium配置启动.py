# coding:utf-8
'''
@author: 猫大白
Project: 初识appium
'''

from appium import webdriver
# 配置项
caps = {
    'platformName':'Android',
    'appPackage':'com.xiaomi.shop',
    'appActivity':'.activity.MainTabActivity',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
driver.implicitly_wait(10)


driver.find_element_by_id('com.xiaomi.shop:id/dialog_btn_agree_yes').click()
try:
    driver.find_element_by_xpath("//*[@text='允许']").click()
except:
    pass
