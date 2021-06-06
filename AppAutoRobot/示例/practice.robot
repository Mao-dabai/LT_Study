*** Settings ***
Library     AppiumLibrary  # 导入指定库


*** Test Cases ***
测试设置字体超大
    Open Application    http://localhost:4723/wd/hub    platformName=Android
    ...                   appPackage=com.android.settings   appActivity=.Settings
    click element       xpath=//*[@text="显示"]
    sleep               5
    click element       xpath=//*[@text="字体大小"]
    sleep               5
    click element       xpath=//*[@content-desc="最大"]
