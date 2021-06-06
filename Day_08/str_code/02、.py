# coding:utf-8
'''
@author: 猫大白
Project:
'''

import base64

from appium import webdriver

caps = {
    'platformName': 'Android'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# driver.push_file(source_path='/Users/superhin/Downloads/loading.gif',
#                  destination_path='/sdcard/loading.gif')
adb_cmd = {'command': 'ls',
           # 'args': '/sdcard/ | grep "loading.gif"'.split(' '),
           'args': ['/sdcard/', '|', 'grep', '"loading.gif"']
           }
result = driver.execute_script('mobile: shell', adb_cmd)
print('result', result)

file_base64 = driver.pull_file('/sdcard/loading.gif')
file_bytes = base64.b64decode(file_base64)
with open('loading2.gif', 'wb') as f:
    f.write(file_bytes)
