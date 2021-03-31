# coding:utf-8
'''
@author: 猫大白
Project:三种输入方式
'''
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.12306.cn/index/')
js = "document.getElementById('fromStationText').value='北京'"
driver.execute_script(js)
