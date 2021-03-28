# coding:utf-8
'''
@author: 猫大白
Project:Python高级之XPath
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# xpath绝对路径定位
# driver.find_element_by_xpath('/html/body/div/div[2]/div[5]/div/div/form/span[1]/input').send_keys('hh')

# 相对路径结合属性定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys('hahha')
driver.find_element_by_xpath("//input[@id='kw'  and @name='wd']").send_keys('hahha')
driver.find_element_by_xpath("//*[@id='su']").click()



# 相对路径结合节点文本定位
# 完全匹配
driver.find_element_by_xpath("//a[text(),'新闻']").click()
# 包含、、、
driver.find_element_by_xpath("//a[contains(text(),'新')]").click()


# 向上查找
driver.find_element_by_xpath("//td[text()='王五']/../td[4]/a[text()='查看']").click()

# 使用 XPath 轴向前和向后查找
driver.find_element_by_xpath('//*[text()="账号"]/following::input[1]').send_keys('11')
