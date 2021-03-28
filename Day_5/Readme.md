# 浏览器选项
- 常用选项
    - binary_location：用于设置浏览器地址。
    - debugger_address：远程调试地址。
    - headless：设置是否无界面模式。
    - add_argument()：添加启动参数。
    - add_extension()：添加插件。
    - add_encoded_extension()：添加编码后的插件。
    - add_experimental_option()：添加实验选项。
    - to_capabilities()：转为 desired capabilities 格式
- 常用的启动参数如下
    - 禁用图片加载：options.add_argument('blink-settings=imagesEnabled=false')
    - 自动打开开发者工具：options.add_argument("auto-open-devtools-for-tabs")
    - 设置窗口尺寸：options.add_argument('window-size=300,600')
    - 设置窗口启动位置：options.add_argument('window-position=120,0')
    - 禁用 gpu 渲染：options.add_argument('disable-gpu')
    - 全屏启动：options.add_argument('start-fullscreen')
    - 全屏启动，无地址栏：options.add_argument('kiosk')
    - 启动时，不激活（前置）窗口：options.add_argument('no-startup-window')
# XPath定位方式
- 绝对路径定位
    - 阶梯顺序，从1开始
- 相对路径结合属性定位(**建议不要使用class属性**)
    - //标签[@属性] 单属性
    - //标签[@属性 and @属性] 多属性
    - //标签[@属性 or @属性] 多属性
    - //*[@属性]  无标签时使用
- 相对路径结合节点文本查找
    - contains()：包含
        - //标签[text()='文本内容']
        - //标签[contains(text(),'文本内容')]
        - //标签[contains(@属性,'内容')]
    - starts-with()：以特定字符串开头
        - //标签[starts-with(@属性, "字符串")]   
    - last()：最后一个子元素
        - //标签[@属性="字符串"]/同一标签[last()]   
    - normalize-space()：去除左右空白字符
        - //a[normalize-space(text())="新闻"]   
        表示:去除左右空白字符后，文本等于“新闻”的链接。    
- 向上查找：..
    - //td[text()='王五']/../td[4]/a[text()='查看']
- 使用 XPath 轴向前和向后查找
    - following：选取当前节点后的所有节点。
    - following-sibling：选取当前节点后的所有同级节点。
    - preceding：选取当前近节点前的所有节点。
    - preceding-sibling：选取当前节点前的所有同级节点。
# CSS Selector定位方式
- 标签[属性=内容]
    - id可以使用#代替
        - input#kw
    - class可以使用.代替
        - input.btn.self-btn
- 空格/>:向下级查找
- first-child：查找第一个元素
- nth-child(n)：查找第 n 个子元素
# 模拟键盘和鼠标操作
 *Note:页面有刷新，action需要重新定义*
 - 导包
    ```python
    # 模拟键盘包
    from selenium.webdriver.common.keys import Keys
    # 模拟鼠标包
    from selenium.webdriver.common.action_chains import ActionChains
    ```
- 步骤
    - 导入所要使用的包
    - 实例化对象
- ActionChains 对象支持以下元素操作。
    - click()：点击。
    - send_keys()：输入。
    - send_keys_to_element()：向元素输入。
    - double_click()：双击。
    - context_click()：右键单击。
    - click_and_hold()：点击并按住不放。
    - drag_and_drop()：拖动元素 1 到元素 2 位置。
    - move_to_element()：移动到元素。
    - pause()：暂停等待。
    - key_down()：按下键。
    - key_up()：松开键。
    - release()：松开鼠标。
# 等待与期望条件
- 三种等待方式
    - 强制等待
        - time.sleep
    - 智能等待
        - driver.implicitly_wait(5)
    - 显性等待（默认0.5s一次）
        - 导包（from selenium.webdriver.support.wait import WebDriverWait）
        - 声明一个实例化对象
        - 实例化对象.util(期望条件)
- 期望条件
    - 导包（from selenium.webdriver.support import expected_conditions as EC）
    - 方法看源码
    
# JavaScript运用
- JS查找元素
    - 查找单个元素：
        - document.getElementById()：使用元素 id 查找元素。
        - document.querySelector()：使用 CSS Selector 查找元素。
    - 查找多个元素：
        - document.getElementsByName()
        - document.getElementsByClassName()
        - document.getElementsByTagName()
- JS去除限制属性
    - 元素.removeAttribute('属性名')
- 执行JS脚本的四种方式
    - 方法一：执行js脚本
    ```python
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    js = 'document.querySelector("#kw").value="我是谁"'
    driver.execute_script(js)
    ```
    - 方法二：执行多行js脚本
    ```python
    js1 = """
    var elm = document.querySelector("#kw");
    elm.setAttribute('style', 'background: yellow; border: 2px solid red')
    """
    driver.execute_script(js1)
    ```
    - 第三种方式：return返回值
    ```python
    js2 = 'return document.querySelector("#kw");'
    element = driver.execute_script(js2)
    element.send_keys('我是谁')
    ```
    - 第四种方式：参数化脚本
    ```python
    element = driver.find_element('id', 'kw')
    style='background: green; border: 2px solid red;'
    js3 = 'arguments[0].setAttribute("style", arguments[1]);'
    element = driver.execute_script(js,element,style)
    ```
- 页面滚动

# Page Object Model

