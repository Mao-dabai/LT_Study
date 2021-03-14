# coding:utf-8
'''
@author: 猫大白
Project:Python的包和模块
'''
# 常用模块time、random

import time

print(time.time()) # 时间戳：1545276241.5708632
print(time.localtime()) # 本地时区的struct_time
print(time.strftime("%Y-%m-%d%H:%M:%S")) # 格式化的时间字符串:'2018-12-2011:30:50'
print(time.strftime("%Y-%m-%d%X")) # 格式化的时间字符串:'2018-12-2011:30:50'X：表示小时分钟秒


import random
print(random.random()) # (0,1)----float大于0且小于1之间的小数
print(random.randint(1,3)) # [1,3]大于等于1且小于等于3之间的整数
print(random.randrange(1,3)) # [1,3)大于等于1且小于3之间的整数
print(random.choice([1,'23',[4,5]])) # 1或者23或者[4,5]