# python的四大容器
## list -- 列表
- 定义
    - list = [1,2]
- 增加  
    - append：追加，默认最后一位
    - insert：基于索引在任意插入元素
    - extend：迭代着追加，在列表的最后面迭代追加一组数据
- 删除    
    - pop：通过索引删除列表中对应的元素，该方法返回删除的元素
    - remove：通过元素删除列表中的该元素
    - clear：清空列表
    - del list[index]：基于列表索引删除元素
- 修改
    - list[index]:基于索引修改元素 
    - list[start_index,end_index]:按照切片改值
    - list[::step]:按照步长改值
- 查询
    - in:元素是否在列表中
- 排序
    - list.sort():从小到大排序
    - list.sort(reverse=True):从大到小排序
## tuple -- 元组
- 定义
    - a(1,)
- 查询
    - index：基于元素查元组中该元素的索引
    - count:查询元素在元组中出现的次数
 - 嵌套修改
 >元组本身不支持修改，但是元组中如果有支持修改的元素，可以使用嵌套修改
## dict -- 字典
- 定义
    - dict = {key:value}
- 添加
    - dict[key] = value # key不存在即添加
- 删除
    - del dict[key]  # 基于键删除
- 修改
    - dict[key] = value # key存在即修改
- 查询
    - dict.get(key) # 通过key查询对应value    
- 取键
    - dict.keys()  # 取字典中所有的key
- 取值
    - dict.values()  # 取字典中所有的value    

## set -- 集合
>有自动去重功能
- 定义
    - set = {1,2,3,4}
- 添加
    - add：添加一个元素，默认最后一位
- 删除
    - remove：删除指定元素
    - pop：随机删除一个元素
    - clear：清空集合
# 文件相关
- 文件操作
```python
# 打开文件；有则打开，无则创建
f = open('文件路径',mode='w',encoding='utf-8')
f.write('hello')  
f.close()  
```
- mode语法含义
    - w：只写；有则覆盖
    - r：只读
    - a：追加；无则写入，有则追加
- 常用操作
    - read(number):限制几个文字，默认全部读取
    - readlines():返回一个列表，读取全部；每一行结束后包含\n
    - readline():只读取一行
- 另一种打开方式
```python
with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt',mode='r') as f:
    data = f.read()
    print(data)
    f.close()
```
# 函数相关
- 函数可以解决什么问题？
    - 代码的组织结构不清晰，可读性差
    - 遇到重复的功能智能重复编写实现代码，代码冗余
    - 功能需要扩展时，需要找出所有实现该功能的地方修改之，无法统一管理且维护难度极大
- 函数分类
    - 内置函数
    - 自定义函数
    - pass - 空函数
- 函数的定义
```
def 函数名():
    函数体 代码
    return  返回值
```
- 函数的调用
>程序本身不会自动执行函数，需要调用执行
```
函数名()
```
- 定义函数的三种形式
    - 有参函数
    >定义时有参，调用时需传参
    - 无参函数
    >定义时无参，调用时无需传参
    - 空函数
- return返回值
    - 无值，返回None
    - 有单个值，返回单个值
    - 有多个值，返回一个包含多值的元组
    
- 参数分类
    - 缺省参数
        >定义的函数参数有默认值；传入实参则取实参，不传入则用默认值
    - 不定长参数
        - 动态参数：*args
            >会把位置参数转化为一个tuple
        - 关键字参数：**kwargs
            >会把关键字参数转化为一个dict    
- 参数顺序
    - 位置参数、*args、默认参数、**kwargs
    