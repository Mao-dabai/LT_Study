# coding:utf-8
'''
@author: 猫大白
Project:POM
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class HomePage:
    login_lnk = (By.LINK_TEXT,'登录')
    search_ipt = (By.ID,'search')
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def click_login_lnk(self):
        self.driver.find_element(*self.login_lnk).click()

    def search(self,keyword):
        self.driver.find_element(*self.search_ipt).send_keys(keyword+Keys.ENTER)

class LoginPage:
    username_ipt = (By.ID,'username')
    password_ipt = (By.ID,'pwd')
    login_btn = (By.ID,'login-button')
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def enter_username(self,username):
        print(f'输入用户名{username}')
        elm = self.driver.find_element(*self.username_ipt)
        elm.clear()
        elm.send_keys(username)

    def enter_password(self,password):
        elm = self.driver.find_element(*self.password_ipt)
        elm.clear()
        elm.send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()


