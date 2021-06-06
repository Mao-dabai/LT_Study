*** Settings ***
Library     AppiumLibrary

*** Keywords ***
启动小米商城
    open application    http://localhost:4723/wd/hub
    ...                 platformName=Android    appPackage=com.xiaomi.shop
    ...                 appActivity=.activity.MainTabActivity   noReset=True
    sleep       6
点击分类
    click text          分类

点击小米手机
    click text          小米手机



*** Test Cases ***
测试点击分类
    启动小米商城
    点击分类
    点击小米手机


