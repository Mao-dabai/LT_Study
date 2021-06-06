*** Settings ***
Library     AppiumLibrary
Resource    ./基础操作.robot
Resource    ./分类页.robot
Resource    ./首页.robot
Resource    ./data/config.robot

*** Test Cases ***
测试点击分类
    启动小米商城      ${appium_server}    ${MuMu}
    点击分类
    点击小米手机


