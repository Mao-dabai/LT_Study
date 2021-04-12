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
## 两种形式
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

# Python进阶
## 装饰器
- 定义：在不改变原函数的情况下对函数进行补充改造
- AOP:面向切面编程
- 本质：用来处理函数的函数---高级函数
- 使用场景：
    - 参数校验
    - 返回值格式化
    - 加日志
    - 权限管理
    - 登记
- 装饰器种类
    - 基础装饰器
    - 处理函数参数
    - 带参装饰器
## 迭代器和生成器
- 迭代器
    - 定义：逐个输出一批数据
    - 可迭代意味着可遍历数据（字符串、列表、元组、字典、集合、文件、句柄。。。）
- 生成器
    - 定义：内部实现了迭代器的一种函数式写法，通过yield记录当前位置并返回一次迭代结果
    - 优点：基于推理生成数据，一次生成一个或一行，节省内存
- yield和return的区别
    - yield 不会结束，只是暂停
    - return 直接结束
    


## 推导式
- 作用：快速创建列表、字典
- 格式
    - list:[表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件]
    - dict:{ key:value for key,value in existing_data_structure }
    - set:{ expression for item in Sequence if conditional }

## 魔术方法
- 定义：python中内置的__aa__格式的
- 常见的魔术方法：

     魔术方法 | 描述
    ---|---
    __new__| 创建类并返回这个类的实例
    __init__ | 可理解为“构造函数”，在对象初始化的时候调用，使用传入的参数初始化该实例
    __del__  | 可理解为“析构函数”，当一个对象进行垃圾回收时调用
    __metaclass__ | 定义当前类的元类
    __class__ | 查看对象所属的类
    __base__ | 获取当前类的父类
    __bases__ | 获取当前类的所有父类
    __str__ | 定义当前类的实例的文本显示内容
    __getattribute__ | 定义属性被访问时的行为
    __getattr__ | 定义试图访问一个不存在的属性时的行为
    __setattr__ | 定义对属性进行赋值和修改操作时的行为
    __delattr__  | 定义删除属性时的行为
    __copy__ | 定义对类的实例调用 copy.copy() 获得对象的一个浅拷贝时所产生的行为
    __deepcopy__ | 定义对类的实例调用 copy.deepcopy() 获得对象的一个深拷贝时所产生的行为
    __eq__ |定义相等符号“==”的行为
    __ne__ |定义不等符号“!=”的行为
    __lt__ |定义小于符号“<”的行为
    __gt__ |定义大于符号“>”的行为
    __le__ |定义小于等于符号“<=”的行为
    __ge__| 定义大于等于符号“>=”的行为
    __add__| 实现操作符“+”表示的加法
    __sub_|实现操作符“-”表示的减法
    __mul__ |实现操作符“*”表示的乘法
    __div__ |实现操作符“/”表示的除法
    __mod__| 实现操作符“％”表示的取模(求余数)
    __pow__| 实现操作符“**”表示的指数操作
    __and__| 实现按位与操作
    __or__ | 实现按位或操作
    __xor__ | 实现按位异或操作
    __len__ | 用于自定义容器类型，表示容器的长度
    __getitem__| 用于自定义容器类型，定义当某一项被访问时，使用 self[key] 所产生的行为
    __setitem__ | 用于自定义容器类型，定义执行 self[key]=value 时产生的行为
    __delitem__ | 用于自定义容器类型，定义一个项目被删除时的行为
    __iter__ | 用于自定义容器类型，一个容器迭代器
    __reversed__ | 用于自定义容器类型，定义当 reversed( ) 被调用时的行为
    __contains__ |用于自定义容器类型，定义调用 in 和 not in 来测试成员是否存在的时候所产生的行为
    __missing__ | 用于自定义容器类型，定义在容器中找不到 key 时触发的行为