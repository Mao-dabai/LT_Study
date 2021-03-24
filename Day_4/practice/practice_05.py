# coding:utf-8
'''
@author: 猫大白
Project:
'''
# 一、python基础
# 1、列表操作
l = ['a','b','a','c','d','c','a','e','f','a','a','b','a','c']
print('l的列表反转结果：',l[::-1])
l.sort()
print('l的列表排序结果：',l)
print('l的去重结果：',set(l))
for i in set(l):
    print('%s的出现个数为%d次'%(i,l.count(i)))

# 2、两个不重复列表a1=[1,2,5,6,8,9] a2=[2,3,5,6,1,4,3,7]，找到其中相加为10的
a1 = [1,2,5,6,8,9]
a2 = [2,3,5,6,1,4,3,7]
for i in a1:
    for j in a2:
        if i+j==10:
            print(i,j)

# 3、封装一个函数，根据传入的参数如’chrome’，来启动不同的浏览器，并返回driver
from  selenium  import webdriver
def start(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print('输入有误！')
    return driver

# 4、封装一个元素查找方法,传入driver,定位方式，定位表达式（元素属性），根据定位方式进行定位，并返回定位到的元素。
@start
def find(driver,by,value):
    if by == 'id':
        A = driver.find_element_by_id(value)
        return A
    elif by == 'name':
        A = driver.find_element_by_name(value)
        return A
    elif by == 'class_name':
        A = driver.find_element_by_class_name(value)
        return A
    elif by == 'tag_name':
        A = driver.find_element_by_tag_name(value)
        return A
    elif by == 'link_text':
        A = driver.find_element_by_link_text(value)
        return A
    elif by == 'partial_link_text':
        A = driver.find_element_by_partial_link_text(value)
        return A
    elif by == 'xpath':
        A = driver.find_element_by_xpath(value)
        return A
    elif by == 'css_selector':
        A = driver.find_element_by_css_selector(value)
        return A
    else:
        print('无此元素定位方法！')

# 5、封装一个通过id定位函数，当查找元素报错时，对当前页面进行截图，并按当前时间命名str(time.time())
import time
def find_by_id(driver,value):
    try:
        A = driver.find_element_by_id(value)
    except Exception():
        a = str(time.time())+'.png'
        A.screenshot(a)

# 二、面试题
"""
## 你们公司自动化是怎么做的？
- 1、制定测试计划
- 2、搭建测试环境
- 3、编写测试用例
- 4、执行测试用例并分析

## WebDriver的原理是什么，基于什么模式？
- WebDriver是一套基于HTTP的API协议
- 工作原理：
	- 使用不同的浏览器驱动，启动一套WebDriver服务
	- 测试脚本通过调用不同的Selenium SDK的方法将代码转化为API接口发送给驱动的WebDriver服务
	- 驱动将API请求转化为浏览器操作指令，控制浏览器完成操作

## Selenium有几种定位方式？你最常使用哪种？
- id、name、class_name、tag_name、link_text、xpath、css_selector
- 常用：css_selector、xpath

## 对话框怎么处理？
- 模态框：直接定位即可
- alert弹窗：需要switch_to.alert()后再操作
- 新窗口：不用处理；若需要进入新窗口，需要switch_to.window(new_window_handel)

## 元素定位不到怎么处理？
- 找到该元素的父节点/祖先节点，依次阶梯定位

## 一个元素没有id、name、class属性该如何定位，如何定位id属性动态变化的元素？
- 通过xpath定位

## 怎么判读页面上一个元素是否存在？
```python
# 第一种方法
try:
	driver.find_element_by_id('元素名')
except Exception:
	print('元素不存在！')

# 第二种方法
A = driver.find_elements_by_id('元素名')
if len(A) == 0:
	print('元素不存在！')
else:
	print('元素存在！')

```

## 自动化流程中遇到嵌入式页面（框架页面）如何处理？
- 需要进行框架切换---switch_to.frame(id/name)
## 怎么对一个元素进行截图？
```python
A = driver.find_element_by_id('元素')
A.screenshot('a.png')
```
## Web自动化中怎么处理上传下载？
- 上传：定位元素直接send_keys(file_path)
- 下载：定位元素直接click()


"""

