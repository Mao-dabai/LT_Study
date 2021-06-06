# coding:utf-8
'''
@author: 猫大白
Project:
'''

# from appium import  webdriver
#
# caps = {
#     "platformName" : "Android",
#     "platformVersion" : "7.1.2",
#     "appPackage" : "com.xiaomi.shop",
#     "appActivity" : ".activity.MainTabActivity",
#     "autoLaunch": False
# }
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# driver.implicitly_wait(10)
#
# driver.start_activity("com.xiaomi.shop","com.xiaomi.passport.ui.page.AccountLoginActivity")
#
# driver.find_element_by_id("com.xiaomi.shop:id/action_goto_psw_signin").click()
#
# driver.find_element_by_id('com.xiaomi.shop:id/userId').send_keys("18010181267")
# driver.find_element_by_id('com.xiaomi.shop:id/password').send_keys('helloworld')
# driver.find_element_by_id('com.xiaomi.shop:id/sign_in_btn').click()
#
#

from appium import webdriver
from time import sleep
caps = {}
caps['platformName'] = 'Android'  # 必选
caps['appPackage'] = 'com.xiaomi.shop'
caps['appActivity'] = '.activity.MainTabActivity'
caps['autoLaunch'] = False

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(10)
print('启动app')
driver.launch_app()

print('启动登录页')
driver.start_activity('com.xiaomi.shop', 'com.xiaomi.passport.ui.LoginActivity')

driver.find_element_by_xpath('//*[contains(@text,"用帐号密码登录")]').click()
sleep(0.5)
input_list = driver.find_elements_by_class_name('android.widget.EditText')

print('输入框个数', len(input_list))

input_list[0].send_keys('18010181267')
input_list[1].send_keys('helloworld')

driver.find_element_by_xpath('//*[@text="登录"]').click()
