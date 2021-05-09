from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('https://www.mi.com')
driver.maximize_window()
driver.find_element_by_link_text('登录').click()
sleep(1)
try:
    driver.find_element('xpath', "//*[text()='同意']").click()
except:
    pass
sleep(1)
# assert '小米帐号 - 登录' == driver.title

# 登录
driver.find_element('name', 'account').send_keys('13582105112')
driver.find_element('name', 'password').send_keys('xk940819zj')
driver.find_element('class name', 'mi-button').click()
sleep(1)

# 搜索
driver.find_element('id', 'search').send_keys('小米电视')
driver.find_element('class name', 'search-btn').click()
driver.find_elements('class name', 'goods-item')[1].click()

# 切窗口
driver.switch_to.window(driver.window_handles[-1])

# 加购
driver.find_element('link text', '加入购物车').click()
sleep(1)
driver.find_element('link text', '去购物车结算').click()
sleep(1)

# 去结算
driver.find_element('link text', '去结算').click()
sleep(1)
driver.find_elements('class name', 'address-item')[0].click()
driver.find_element('link text', '去结算').click()

driver.find_element('link text', '我的订单').click()
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
driver.find_element('link text', '订单详情').click()
sleep(1)
driver.find_element('link text', '取消订单').click()
sleep(1)
driver.find_element('xpath', "//button[@class='btn btn-primary']").click()

driver.close()
