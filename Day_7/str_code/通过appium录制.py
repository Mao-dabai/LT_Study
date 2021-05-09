# coding:utf-8
'''
@author: 猫大白
Project:录制的代码
'''
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.xiaomi.shop"
caps["appActivity"] = ".activity.MainTabActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xiaomi.shop:id/dialog_btn_agree_yes")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView")
el3.click()
el4 = driver.find_element_by_accessibility_id("搜索")
el4.click()
el5 = driver.find_element_by_id("com.xiaomi.shop2.plugin.search:id/input")
el5.send_keys("小米11")
el6 = driver.find_element_by_id("com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn")
el6.click()
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
el7.click()

driver.quit()
