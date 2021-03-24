# coding:utf-8
'''
@author: 猫大白
Project:爬虫实践
'''
# 1.访问https://movie.douban.com/top250 ，翻页并输出所有的top250电影名称、导演及主演
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://movie.douban.com/top250')
driver.maximize_window()

data = driver.page_source
# print(data)
pattern = 'alt="(.*?)"'
A = re.findall(pattern=pattern,string=data)

pattern1 = '<p class="">"(.*?)"</br>'

B = re.findall(pattern=pattern1,string=data)

print(A,B)
driver.quit()