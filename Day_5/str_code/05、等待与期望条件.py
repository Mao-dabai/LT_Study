# coding:utf-8
'''
@author: 猫大白
Project:Selenium的等待策略
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 强制等待
from time import sleep
sleep(3)

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html#')

# 智能等待（隐形等待）
# 10s是最大超时时间
driver.implicitly_wait(10)

# 重试次数
# for i in range(10):
#     try:
#         driver.find_element_by_xpath('11')
#     except NoSuchElementException:
#         sleep(1)
#     break

# 显性等待（轮询等待）
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver,10)
# 第一种方式
# def find_View(driver):
#     return driver.find_element_by_xpath("//td[text()='王五']/../td[4]/a[text()='查看']")
# elm = wait.until(find_View)

# 第二种方式
elm = wait.until(lambda driver:driver.find_element_by_xpath("//td[text()='王五']/../td[4]/a[text()='查看']"))
elm.click()


# 期望条件
from selenium.webdriver.support import expected_conditions as EC

locator = ('xpath',"//td[text()='王五']/../td[4]/a[text()='查看']")
wait.until(EC.presence_of_all_elements_located(locator))

