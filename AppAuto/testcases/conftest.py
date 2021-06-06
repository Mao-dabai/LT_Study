import os


import pytest
import yaml
from appium import  webdriver

from pages.home_page import HomePage
from pages.category_page import CategoryPage

@pytest.fixture()
def config(request):   # pytest系统fixture
    rootdir = request.config.rootdir  # 拿到项目根路径
    file_path = os.path.join(rootdir,'data','config.yaml')  # 配置文件路径
    with open(file_path,encoding='utf-8') as f:
        data = yaml.safe_load(f)  # 转为字典
        return data
    
    
@pytest.fixture()
def appium_server(config):
    """获取配置中appium服务器地址"""
    return config['appium_server']


@pytest.fixture()
def get_app(config):
    """提供一个函数，可以根据apps配置的应用名选择被测应用"""
    apps = config['apps']
    
    def _get_app(name):
        return apps.get(name,{})
    return _get_app


@pytest.fixture()
def get_device(config):
    """提供一个函数，可以根据devices配置的设备名选择被测设备"""
    devices = config['devices']

    def _get_device(name):
        return devices.get(name,{})
    return _get_device


@pytest.fixture()
def driver(appium_server,get_app,get_device):
    caps = {}
    caps['noReset'] = True
    app = get_app('mishop')
    device = get_device('MuMu')
    caps.update(app)
    caps.update(device)
    dr = webdriver.Remote(appium_server, caps)
    dr.implicitly_wait(20)
    yield dr
    dr.quit()

@pytest.fixture()
def home(driver):
    """首页对象"""
    return HomePage(driver)

@pytest.fixture()
def category(driver):
    """分类页面"""
    return CategoryPage(driver)
