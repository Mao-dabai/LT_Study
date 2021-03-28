# coding:utf-8
'''
@author: 猫大白
Project:
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

class baidu_page():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    search_ipt = (By.ID,'kw')
    submit_btn = (By.ID,'su')
    def url_conn(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def search(self,keyword):
        print(f'关键字:{keyword}')
        elm = self.driver.find_element(*self.search_ipt)
        elm.clear()
        elm.send_keys(keyword)

    def submit(self):
        self.driver.find_element(*self.submit_btn).click()

driver = webdriver.Chrome()
page = baidu_page(driver)

page.url_conn('https://baidu.com')
page.search('我是谁')
page.submit()