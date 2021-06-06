*** Settings ***   # 设置
Library     AppiumLibrary   # 导入一个三方库
Library     ./自定义库.py    # 导入自定义库
Resource    ./资源1.robot    # 导入资源
Variables   ./变量.py
Documentation   测试示例    # 说明文档
Metadata        a=1        # 源数据

Suite Setup   log to console  测试套件准备
Suite Teardown   log to console  测试套件清理
Test Setup   log to console  用例准备
Test Teardown   log to console  用例清理

Force Tags      demo    # 示例
Default Tags    测试

*** Variables ***  # 全局变量
${a}        hello,world     # string
${b}        123     # string
@{c}        1   2   3   # list
&{d}        a=1     b=2     c=3     # dict

*** Keywords ***   # 用户关键字（自定义函数）
加法



*** Test Cases ***   # 用例
测试1
    [Documentation]     用例1说明
    [Tags]      示例1     web
    log to console  ${a}
    log to console  ${b}
#    click category
#    clcik xiaomi

测试2
    log to console      hello,world
    log to console      ${a}
    log to console      ${b}
#    log to console      @{c}   # 报错
    log to console      ${c}
#    log to console      &{d}   # 报错
    log to console      ${d}

测试3
    ${e}    Set Variable    hi,gitl     # string
    @{f}    Create List      a   b   c  # list
    &{g}    Create Dictionary   name=kevin  age=12  # dict
    log to console  ${e},你好pl ${f} ${g}

测试4