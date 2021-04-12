# 框架
- 什么是框架？
```text
框架是应用的组织架构，一般包含代码、配置、数据、日志、依赖的组织，可复用模块
的抽取以及运行控制等；
```
- 框架的基本功能构成
    - 代码、配置文件、数据文件等的分类组织
    - 依赖管理
    - 公共模块的复用
    - 运行流程及控制
- 测试框架的优点
    - 用例执行互相独立，一个用例失败不影响其他用例执行和验证。
    - 清晰的用例执行状态，如成功、失败、出错、跳过等以及系统的测试报告。
    - 灵活的用例挑选及批量运行。
    - 提供丰富的断言（期望结果与实际结果的对比）方法。
    - 提供不同范围的测试准备和清理方法。
    - 在特定环境不满足条件时，跳过用例

# Pytest框架
## 格式要求
- 模块名：test开头
- 函数名：test开头
- 函数级
    - 前置函数：setup_function()
    - 后置函数：teardown_function()
- 方法级
    - 前置函数：setup_method()
    - 后置函数：teardown_method()
- 类级
    - 前置函数：setup_class()
    - 后置函数：teardown_class()
- 模块级：
    - 前置函数：setup_module()
    - 后置函数：teardown_module()
## 运行pytest脚本方法
- 命令行执行
    - pytest 模块名
        - -v  详细模式，console中显示用例名
        - -q  安静模式，console中不显示设备信息
        - -s  停止捕获，把输出显示在console中
    - pytest 模块名::类名::要执行的脚本名
- 代码执行
```python
if __name__ == '__main__':
    pytest.main(['test_baidu2.py','-qs'])
```
- 生成报告命令
    - pytest 模块名::类名::函数名 --html=report.html --self-contained-html
## Fixture使用
- 什么是Fixture？
    - Fixtures 函数是 Pytest 的精髓之处
    - 使用@pytest.fixture 装饰器即可快速将函数转为
      Fixture 函数
    - Fixture 函数中可以即包含 setup 测试准备及 teardown 测试清理步骤，使用 yield
      隔开
- Fixtures 方的主要使用方式有 3 种：
    - 1、Fixtures 函数名直接作为用例参数使用（参数结果及 Fixture 方法返回值）
    - 2、在用例上使用@pytest.mark.userfixtures("fixture的函数名")；
    - 3、Fixture 方法上使用 autouse=True 来使用例自动使用。
- Fixture的参数
    - scope 范围
        - class  类
        - module  模块
        - package 包
        - session 会话
    - autouse = True  自动使用
    - params    参数化
- 工厂方法
    - fixture中使用函数嵌套
- 数据驱动   
```python
from time import sleep
import pytest
DATA = ['张三','李四','临渊']
@pytest.mark.parametrize('keyword',DATA)
def test_baidu_search2(driver,keyword):
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    
    driver.find_element('id', 'kw').send_keys(keyword)
    driver.find_element('id', 'su').click()
    sleep(1)
    assert keyword in driver.title
```
-  conftest
    - 共享fixture
    - 钩子
    - 导入路径
# 从脚本到框架