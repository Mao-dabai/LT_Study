# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 1、启动小米商城
# 2、首页-->点击分类
# 3、分类页-->小米手机
# from appium import webdriver
# from time import  sleep
# caps = {
#     "platformName":"Android",
#     "platformVersion":"7.1.2",
#     "udid":"127.0.0.1",
#     "appPackage":"com.xiaomi.shop",
#     "appActivity":".activity.MainTabActivity",
#     "noReset":True
# }
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
# driver.implicitly_wait(10)
# sleep(5)
#
#
# driver.find_element_by_xpath("//*[@text='分类']").click()
# driver.find_element_by_xpath("//*[@text='小米手机']").click()


def test_category(home,category):
    home.click_category()
    category.click_xiaomi_mobile()