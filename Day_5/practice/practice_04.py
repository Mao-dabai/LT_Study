# coding:utf-8
'''
@author: 猫大白
Project:
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.miniui.com/demo/datepicker/datepicker.html')
js = """
var elm = document.getElementById('date3$text');
elm.removeAttribute('readonly');
elm.value='2020-04-03'
"""

driver.execute_script(js)