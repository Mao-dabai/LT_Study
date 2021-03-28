# coding:utf-8
'''
@author: 猫大白
Project:Selenium之JavaScript
'''
from selenium import webdriver
# JS查找元素，去除属性
# document.getElementById('ds').removeAttribute('disabled')
# document.getElementById('hd3').removeAttribute('style')
# document.getElementById('ro').removeAttribute('readonly')
# document.getElementById('hd1').removeAttribute('hidden')


# 执行js脚本
# 方法一：执行js脚本
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
js = 'document.querySelector("#kw").value="我是谁"'
driver.execute_script(js)

# 方法二：执行多行js脚本
js1 = """
var elm = document.querySelector("#kw");
elm.setAttribute('style', 'background: yellow; border: 2px solid red')
"""
driver.execute_script(js1)

# 第三种方式：return返回值
js2 = 'return document.querySelector("#kw");'
element = driver.execute_script(js2)
element.send_keys('我是谁')

# 第四种方式：参数化脚本
element = driver.find_element('id', 'kw')
style='background: green; border: 2px solid red;'
js3 = 'arguments[0].setAttribute("style", arguments[1]);'
element = driver.execute_script(js,element,style)



# driver.quit()

# TODO 页面滚动
