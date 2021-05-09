- 1、从appium导入webdriver
    - pip install appium-python-client
        ```python
      from appium import webdriver
        ```
- 2、新建一个字典描述期望配置
```python
caps = {
    # 平台要求
    'platformName':'Android',             # 设备类型（必填）
    # 'platformVersion':'7.1.2',          # Android版本（可忽略）
    # 设备要求
    # 'deviceName': '127.0.0.1:62001',    # 限制设备（可忽略）
    # 应用要求
    # 手动安装-给定包名和入口门
    'appPackage':'com.xiaomi.shop',
    'appActivity':'.activity.MainTabActivity',
    # 自动安装-给定安装包路径
    # 'app':r'D:\python_src\python_appium\apk_package\xiaomi.apk'
}
```
- 3、连接Appium服务指定的接口，传入期望值
```python
driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
```
- 4、定位元素
    - 通过id定位
    ```python
    driver.find_element_by_id('com.xiaomi.shop:id/dialog_btn_agree_yes').click()
    ```