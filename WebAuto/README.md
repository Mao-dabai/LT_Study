# WebUI自动化测试框架
>基于selenium+pytest


## 框架结构
```shell script
WebAuto/
    data/     # 数据目录
    pages/    # 页面对象模型
      base_page.py   # 页面对象基础类
    testcases/    # 测试用例目录
      __init__.py  # 配合conftest.py导入项目根目录
      conftest.py  # 测试辅助方法集合
    pytest.ini    # pytest的测试配置
    README.MD     # 项目说明
    requirements.txt   # 项目依赖
```

## 使用方法
- 1、复制或下载本程序（不包含venv）
- 2、cd WebAuto
- 3、新家虚拟环境（可忽略）
- 4、安装依赖
    ```shell script
    pip install -r requirements.txt
    ```
- 5、（新页面）对编写Page Object模型
