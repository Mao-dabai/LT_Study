# coding:utf-8
'''
@author: 猫大白
Project:
'''
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/Administrator/Desktop/selenium_demo/selenium_demo/selenium.html')
elm = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[3]/label[2]/input')
if elm.is_selected() is False:
    elm.click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/input').send_keys(r'D:\LTTest_Study\Day_4\picture\qq.png')
sleep(3)

driver.quit()