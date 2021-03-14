# Python异常处理
## 什么是异常？
- 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
- 一般情况下，在Python无法正常处理程序时就会发生一个异常。
- 异常是Python对象，表示一个错误
## 为什么要处理异常？
- python解释器执行代码时，若遇到异常后面程序将不会执行；
- 所以必须提供一种异常处理机制来增强你程序的健壮性与容错性
## 处理异常的方法
- 方法
    ```
    try:
        要运行代码
    except 异常类型:
        提示代码
    ```
- 异常类型：
    - NameError：变量未定义
    - ZeroDivisionError：除数为0
    - FileNotFoundError：文件找不到
- 万能异常Exception
    ```python
    try:
        print(num)
        11/0
    except Exception as a:
        print(a)  # 只打印第一个错误
        print('捕获异常2！！！')
    ```
# Python的包和模块
## 什么是模块？
- 模块是一组功能的集合，即一个功能点；

## 调用模块的优点
- 拿来主义
- 结构清晰，方便管理
- 提高代码的重复利用率
## 模块使用
- 调用方法
    - import 模块名
    - from 包名.模块名/模块名 import 函数名1,函数名2
    - from 包名.模块名/模块名 import *
    - from 包名.模块名/模块名 import 函数名1 as 新的函数名
- 常用模块介绍
    - time：时间模块
    ```python
    import time
    print(time.time()) # 时间戳：1545276241.5708632
    print(time.localtime()) # 本地时区的struct_time
    print(time.strftime("%Y-%m-%d%H:%M:%S")) # 格式化的时间字符串:'2018-12-2011:30:50'
    print(time.strftime("%Y-%m-%d%X")) # 格式化的时间字符串:'2018-12-2011:30:50'X：表示小时分钟秒
    ```
    - random:生成随机数
    ```python
    import random
    print(random.random()) # (0,1)----float大于0且小于1之间的小数
    print(random.randint(1,3)) # [1,3]大于等于1且小于等于3之间的整数
    print(random.randrange(1,3)) # [1,3)大于等于1且小于3之间的整数
    print(random.choice([1,'23',[4,5]])) # 1或者23或者[4,5]
    ```
# 命名空间
- 全局变量
>在函数外声明的变量，都是全局变量
- 局部变量
>在函数中的变量，是局部变量

- **<font color='red'> Note：局部变量对全局变量可以引用，但是不能修改。 </font>**

# 面向对象编程
## 俩种形式
- 面向对象
>根据业务逻辑从上到下写代码
- 面向过程
>将数据与函数绑定到一起，进行封装，这样能够更快速的开发程序，减少了重复代码的重写过程

## 类和对象
- 类是创建对象的模板，只谈概念就是类
- 对象就是看得见摸得着的实体
```python
#  定义类
class Cat():
    # 定义方法
    def eat(self):
        print('猫在喝水。。。。')

# 创建对象
# 对象名  = 类名()
tom = Cat()
# 调用
# 对象名.方法名
tom.eat()
```
## 属性
```python
class Cat():
    # 初始化
    def __init__(self,name,age):
        # 属性
        # 添加并赋值
        self.name = name
        self.age = age
    # 定义方法
    def eat(self):
        print('猫在喝水。。。。')

    def introduce(self):
        print('%s的年龄是：%d'%(self.name,self.age))

# 创建对象
tom = Cat('汤姆',10)
# 调用
tom.introduce()
```
## 特性
- 继承
    - 单继承
    - 多继承
    - 多层继承
- 封装
>有些时候我们不希望把对象的属性公开，就可以把它设为私有，python并没有像其他语言对成员的权限控制系统，默认情况下，python的所有属性都是公有的，可以被访问到，要设成私有，则在前面加双下划线
```python
class Send:
    # 私有方法
    # 方法名前加__即将方法变为私有方法
    def __send_msg(self):
        print('正在发送短信')
    # 公共方法
    def send(self,money):
        if self.money > 100:
            self.__send_msg()
        else:
            print('余额不足，请充值！')

send = Send()
send.send(20)
```
- 多态
