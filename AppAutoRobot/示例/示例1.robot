*** Settings ***
Library     Selenium2Library  # 导入指定库


*** Test Cases ***
测试百度搜索
    Open Browser   https://www.baidu.com  Chrome
    Input Text     id=kw                  袁隆平
    Click Element  id=su
    Close browser