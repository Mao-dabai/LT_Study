import json

from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage

@pytest.fixture
def json_data():
    def func(path):
        with open(path,encoding='utf-8') as f:
            data = json.load(f)
            return data
    return func


@pytest.fixture
def driver():   # 用例辅助--启动关闭浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):  # 用例辅助--登录
    def func(username,password):
        print(f'登录用户:{username}')
        driver.get('https://account.xiaomi.com/fe/service/login/password?_qrsize=180&sid=mi_eshop&qs=%253Fcallback%253Dhttp%25253A%25252F%25252Forder.mi.com%25252Flogin%25252Fcallback%25253Ffollowup%25253Dhttps%2525253A%2525252F%2525252Fwww.mi.com%2525252Findex.html%252526sign%25253DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%25252C%25252C%2526sid%253Dmi_eshop%2526_qrsize%253D180&callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Findex.html%26sign%3DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%2C%2C&_sign=c0455AmnySfgSTjnQ4ptPssEzGw%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=')
        driver.find_element('name', 'account').send_keys(username)
        driver.find_element('name', 'password').send_keys(password)
        driver.find_element('class name', 'mi-button').click()
    return func


@pytest.fixture
def login_page(driver):
    return LoginPage(driver,url='https://account.xiaomi.com/fe/service/login/password?_qrsize=180&sid=mi_eshop&qs=%253Fcallback%253Dhttp%25253A%25252F%25252Forder.mi.com%25252Flogin%25252Fcallback%25253Ffollowup%25253Dhttps%2525253A%2525252F%2525252Fwww.mi.com%2525252Findex.html%252526sign%25253DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%25252C%25252C%2526sid%253Dmi_eshop%2526_qrsize%253D180&callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Findex.html%26sign%3DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%2C%2C&_sign=c0455AmnySfgSTjnQ4ptPssEzGw%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=')


@pytest.fixture
def search(login):
    return search(login)
