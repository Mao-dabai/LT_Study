# coding:utf-8
'''
@author: 猫大白
Project:
'''
from appium import  webdriver

caps = {
    "platform" : "Android",
    "platformVersion" : "7.0.1",
    "appPackage" : "com.xiaomi.shop",
    "appActivity" : ".activity.MainTabActivity"

}

driver = webdriver.Remote("https://localhost:4723/wd/hub",caps)

print("尺寸",driver.get_window_size())
print("显示密度",driver.get_display_density())
print("网络状态",driver.network_connection)
