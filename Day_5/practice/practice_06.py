# coding:utf-8
'''
@author: 猫大白
Project:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage(object):
    username_ipt = (By.NAME, "username")  # 用户名
    password_ipt = (By.NAME, "password")  # 密码
    login_btn = (By.CSS_SELECTOR, "input.button2")  # 登录按钮

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def conn(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_user(self, username):
        print(f'用户名为：{username}')
        self.driver.find_element(*self.username_ipt).send_keys(username)

    def enter_pwd(self, password):
        print('输入用户密码')
        self.driver.find_element(*self.password_ipt).send_keys(password)

    def click_login_btn(self):
        print('点击确定按钮')
        self.driver.find_element(*self.login_btn).click()


class AddGoods(object):
    man_goods_btn = (By.XPATH, '//a[text()="商品管理"]')  # 商品管理
    add_goods_btn = (By.LINK_TEXT, '添加新商品')  # 添加新商品
    goods_name_ipt = (By.NAME, 'goods_name')  # 商品名称
    goods_class_ipt = (By.ID, 'cat_name')  # 输入商品分类
    goods_class_btn = (By.ID, 'treeDemo_cat_id_3_span')  # 选择商品分类
    goods_price_ipt = (By.NAME, 'shop_price')  # 商品价格
    goods_picture_ipt = (By.NAME, 'goods_img')  # 商品图片
    sub_btn = (By.ID, 'goods_info_submit')  # 确定按钮

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump(self):
        print('商品管理-->添加商品')
        self.driver.switch_to.frame('menu_frame')
        self.driver.find_element(*self.man_goods_btn).click()
        sleep(2)
        self.driver.find_element(*self.add_goods_btn).click()

    def switch_frame(self):
        print('框架切换')
        self.driver.switch_to.parent_frame()
        sleep(2)
        self.driver.switch_to.frame('main-frame')

    def enter_goods_name(self, goods_name):
        print(f'录入商品名称为{goods_name}')
        elm = self.driver.find_element(*self.goods_name_ipt)
        elm.clear()
        elm.send_keys(goods_name)
        return goods_name

    def enter_goods_class(self, goods_class):
        print(f'商品分类为：{goods_class}')
        elm = self.driver.find_element(*self.goods_class_ipt)
        elm.clear()
        elm.send_keys(goods_class)
        sleep(1)
        self.driver.find_element(*self.goods_class_btn).click()

    def enter_goods_picture(self, picture_path):
        print('上传商品图片')
        self.driver.find_element(*self.goods_picture_ipt).send_keys(picture_path)

    def enter_goods_price(self, goods_price):
        print(f'录入商品价格为{goods_price}')
        elm = self.driver.find_element(*self.goods_price_ipt)
        elm.clear()
        elm.send_keys(goods_price)

    def click_submit(self):
        print('点击确定按钮')
        self.driver.find_element(*self.sub_btn).click()

    def check(self):
        source = self.driver.page_source
        if '添加商品成功' in source:
            print('商品添加成功')
        else:
            print('商品添加失败')


class GoodList(object):
    good_list_btn = (By.LINK_TEXT, '商品列表')
    view_btn = (By.XPATH, "//span[text()='dell电脑-x']/../../td[13]/a[1]")  # 查看
    del_btn = (By.XPATH, "//span[text()='dell电脑-x']/../../td[13]/a[4]")  # 回收站

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_good_list(self):
        print('点击商品列表按钮')
        self.driver.find_element(*self.good_list_btn).click()

    def view_goods(self):
        print('点击商品的查看按钮')
        self.driver.find_element(*self.view_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.save_screenshot(r'D:\LT_Study\Day_5\picture\dell.png')
        sleep(1)
        self.driver.close()

    def del_goods(self):
        print('删除商品')
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(3)
        self.driver.switch_to.frame('main-frame')
        self.driver.find_element(*self.del_btn).click()
        self.driver.switch_to.alert.accept()

    def check(self):
        if 'dell电脑-x' not in self.driver.page_source:
            print('删除成功')
        else:
            print('删除失败')
driver = webdriver.Chrome()

# 用户登录
login = LoginPage(driver)
login.conn('http://newecshop.longtest.cn/admin/privilege.php?act=login')
login.enter_user('test01')
login.enter_pwd('test888')
login.click_login_btn()

# 添加商品
add = AddGoods(driver)
add.jump()
add.switch_frame()
add.enter_goods_name('dell电脑-x')
add.enter_goods_class('电脑')
add.enter_goods_picture(r'D:\LT_Study\Day_5\picture\dell电脑.jpg')
add.enter_goods_price(3999)
add.click_submit()
add.check()

# 查看商品并删除
good = GoodList(driver)
good.click_good_list()
add.switch_frame()
good.view_goods()
good.del_goods()
good.check()

good.driver.quit()
