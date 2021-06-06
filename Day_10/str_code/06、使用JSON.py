# coding:utf-8
'''
@author: 猫大白
Project:使用json
'''

import json

data_str = '{"name":"李明","age":18,"is_male":true,"job":null}'

# json--->字典
data_dict = json.loads(data_str)
print("json转换为dict：",data_dict)


# 字典--->json

data_json = json.dumps(data_dict,ensure_ascii=False)
print("dict转换为json：",data_json)


# json文件--->字典
with open(r'D:\LTTest_Study\Day_10\files\data.json',encoding='utf-8') as f:
    data_dict = json.load(f)
    print(data_dict)

# 字典--->json文件

