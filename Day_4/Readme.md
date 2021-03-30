# Selenium简介
## 定义
- 本质上是一套基于HTTP的API协议
## 工作原理
- （1）使用不同的浏览器驱动在本地或远程启动一套WebDriver服务（默认绑定9515端口）；
- （2）测试脚本调用不同的Selenium SDK的方法将代码转化为API请求发送到驱动WebDriver服务；
- （3）驱动将收到的API请求转化为浏览器操作指令，控制浏览器完成操作。
## Web UI自动化
### 基本导航方法
- driver.get(url)：打开网页
- driver.title：获取网页标题
- driver.current_url:获取当前网页url
- driver.page_source：获取网页源码
- driver.back():返回上一个页面
- driver.refresh():刷新
- driver.forward()：前进
- driver.save_screenshot(存放路径)：截图
- driver.close():关闭页面
- driver.quit():退出
- driver.maximize_window():最大化窗口
### 元素定位
- 8种定位方式
    - 常见的：id、name、class_name
    - 不常用的：tag_name(标签名)
    - 链接：link_text(完全匹配)、partial_link_text(部分匹配)
    - 高级定位语法：Xpath、CSS Selector
- 语法
    - find_element
        - 正常返回一个元素对象
        - 定位不到，报错
    - find_elements
        - 正常情况下返回一个定位到的所有元素的一个列表
        - 定位不到返回空列表[]
- 元素常用的操作
    - click():点击
    - send_keys():输入文本
    - clear():清空
- 获取元素属性方法
    - tag_name：元素标签名
    - text：元素文本
    - get_attribute('属性名')：获取元素属性
    - is_displayed()：元素是否显示
    - is_enabled()：元素是否可用（如按钮是否可点击）
    - is_selected()：元素是否已选中
    
### 弹窗处理
- 弹窗分类及定位
    - 模态框/div弹窗/DOM框：直接定位
    - alert弹窗框：switch_to.alert
    - conform弹窗：直接在url中添加值
    - 弹出新页面:switch_to.window(new_window_handel)

### 框架切换
- 如何识别有框架？
    - 开发者工具定位到元素，查看元素的路径，如果有 frame 或 iframe 标签，则
元素在框架页面中
    - 页面中发现有多个竖行滚动条，很有可能是通过框架由多个页面组成。
- 切换方法
    - switch_to.frame('')：切入，支持 frame 或 iframe 的 id、name、index和定位到
的 frame 或 iframe 元素
    - switch_to.parent_frame()：切出到父框架
    - switch_to.default_content():跳出所有框架
# HTML语法


 