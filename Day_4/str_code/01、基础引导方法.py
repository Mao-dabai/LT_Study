# coding:utf-8
'''
@author: 猫大白
Project:Selenium基础操作
'''
# 导入
from selenium import webdriver
from time import sleep

# 创建浏览器对象
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Edge()
# driver = webdriver.Opera()

# Chrome/Edge/Opera/360Safe/QQ---> Chromium

# C是大写, 后面有括号
# 1. 查找并启动chromedriver服务,并获取服务地址
# 2. 连接服务地址

# 打开浏览器
driver.get('https://www.baidu.com')

# 最大化窗口
driver.maximize_window()

print(driver.title)  # 网页标题
print(driver.current_url)  # 当前的url
print(driver.page_source)   # 网页源代码
sleep(1)
driver.get('https://www.qq.com')
sleep(1)
driver.back()  # 返回上一个页面
driver.refresh()  # 刷新
sleep(1)
driver.forward()  # 前进

driver.save_screenshot(r'D:\LTTest_Study\Day_4\picture\qq.png')

sleep(3)
# driver.close()   # 关闭当前页面
driver.quit()  # 退出浏览器
