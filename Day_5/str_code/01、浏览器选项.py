# coding:utf-8
'''
@author: 猫大白
Project:浏览器选项配置
'''

from selenium import webdriver
# 无界面运行
def handless():
    options = webdriver.ChromeOptions()  # 自定义浏览器选项
    options.headless = True
    # options.add_argument('--headless')   # 老方法
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.baidu.com')
    print(driver.title)
    driver.quit()



# 启动其它浏览器
def start_360():
    options = webdriver.ChromeOptions()
    options.binary_location= r'D:\Tools\360浏览器\360se6\Application\360se.exe'
    driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\chromedriver78.exe',options=options)
    driver.get('https://www.baidu.com')
    print(driver.title)

    driver.quit()

