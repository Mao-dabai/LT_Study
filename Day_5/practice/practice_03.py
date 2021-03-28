# coding:utf-8
'''
@author: 猫大白
Project:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html#')

wait = WebDriverWait(driver,60)
elm = wait.until(
    lambda driver:driver.find_element_by_xpath("//td[text()='王五']/../td[4]/a[text()='查看']")
)
elm.click()
sleep(3)
driver.switch_to.alert.dismiss()

driver.quit()