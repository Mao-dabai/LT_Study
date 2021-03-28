# coding:utf-8
'''
@author: 猫大白
Project:Python鼠标操作
'''
from time import sleep

from selenium import webdriver

# 导入模拟键盘包
from selenium.webdriver.common.keys import Keys

# 导入模拟鼠标包
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.maximize_window()

setting = driver.find_element_by_id('s-usersetting-top')  # 定位设置元素
# print(setting.text)  # 打印元素文本
# print(setting.get_attribute('name'))  # 打印元素的name

# 声明一个操作对象
action = ActionChains(driver)
# 移动鼠标
# perform--执行
action.move_to_element(setting).perform()

# 点击下拉菜单
sleep(1)
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()