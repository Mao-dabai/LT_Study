# coding:utf-8
'''
@author: 猫大白
Project:使用csv文件
'''


from time import sleep


def test_login(driver,users):
    username,password = users[0]['username'],users[0]['password']
    driver.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    driver.find_element('name','username').send_keys(username)
    driver.find_element('name','password').send_keys(password)
    driver.find_element_by_css_selector('input.button2').click
    sleep(1)
    assert '管理中心' == driver.title

def test_csv(csv_data):
    print(csv_data(r"D:\LTTest_Study\Day_6\file\users.csv"))
