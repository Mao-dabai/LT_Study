# coding:utf-8
'''
@author: 猫大白
Project:requests的post
'''

import requests


def post_01():
    url = "http://newecshop.longtest.cn/admin/privilege.php"
    data = {
        'username': 'test01',
        'password': 'test888',
        'act': 'signin'
    }
    res = requests.post(url,data=data)
    print(res.text)


def post_02():
    url = "https://httpbin.org/post"
    js = {
        'name': '临渊',
        'age': 18,
        "is_male": True,
        "job": None
    }
    res = requests.post(url, json=js)
    # print(res.text)
    print(res.json())


def post_03():
    url = "https://graph.baidu.com/upload"
    f = open('D:\Documents\Downloads\9f96502f0a58584380b525e4fbdda0aa.jpeg','rb')
    res = requests.post(url,files =f)
    print(res.text)


def post_04():
    url = 'http://newecshop.longtest.cn/admin/goods.php?act=add'
    headers = {
        'Cookie': 'ECSCP[lastfilterfile]=80EE692D; ECS_LastCheckOrder=Sun%2C%2006%20Jun%202021%2003%3A36%3A05%20GMT; ECSCP[lastfilter]=a%253A19%253A%257Bs%253A6%253A%2522cat_id%2522%253Bi%253A0%253Bs%253A10%253A%2522intro_type%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_promote%2522%253Bi%253A0%253Bs%253A13%253A%2522stock_warning%2522%253Bi%253A0%253Bs%253A8%253A%2522brand_id%2522%253Bi%253A0%253Bs%253A7%253A%2522keyword%2522%253Bs%253A0%253A%2522%2522%253Bs%253A12%253A%2522suppliers_id%2522%253Bs%253A0%253A%2522%2522%253Bs%253A10%253A%2522is_on_sale%2522%253Bs%253A0%253A%2522%2522%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A8%253A%2522goods_id%2522%253Bs%253A10%253A%2522sort_order%2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A14%253A%2522extension_code%2522%253Bs%253A0%253A%2522%2522%253Bs%253A9%253A%2522is_delete%2522%253Bi%253A0%253Bs%253A10%253A%2522real_goods%2522%253Bi%253A1%253Bs%253A4%253A%2522supp%2522%253Bi%253A0%253Bs%253A12%253A%2522record_count%2522%253Bs%253A3%253A%2522674%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A45%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[lastfiltersql]=U0VMRUNUIGdvb2RzX2lkLCBnb29kc19uYW1lLCBnb29kc190eXBlLCBnb29kc19zbiwgc2hvcF9wcmljZSwgaXNfb25fc2FsZSwgaXNfYmVzdCwgaXNfbmV3LCBpc19ob3QsIHNvcnRfb3JkZXIsIGdvb2RzX251bWJlcixleGNsdXNpdmUsIGludGVncmFsLCAgKHByb21vdGVfcHJpY2UgPiAwIEFORCBwcm9tb3RlX3N0YXJ0X2RhdGUgPD0gJzE2MjI5MjE4MTknIEFORCBwcm9tb3RlX2VuZF9kYXRlID49ICcxNjIyOTIxODE5JykgQVMgaXNfcHJvbW90ZSAsIHN1cHBsaWVyX3N0YXR1cywgc3VwcGxpZXJfaWQgIEZST00gYG5ld2Vjc2hvcGAuYGVjc19nb29kc2AgQVMgZyBXSEVSRSBpc19kZWxldGU9JzAnICBBTkQgaXNfcmVhbD0nMSdBTkQgZy5zdXBwbGllcl9pZCA9IDAgT1JERVIgQlkgZ29vZHNfaWQgREVTQyAgTElNSVQgMCwxNQ%3D%3D; real_ipd=221.223.165.196; ECSCP_ID=c7bcb0d77b78235275b2a3ae1ca6471a21e28804'
    }
    data = [
        ('MAX_FILE_SIZE', 2097152),
        ('goods_name', 'dell电脑韩志超4'),
        ('goods_sn', None),
        ('cat_name','电脑'),
        ('cat_id',None),
        ('addedCategoryName',None),
        ('other_cat[]', 0),
        ('brand_search', '请输入……'),
        ('brand_search_bf',None),
        ('brand_search_jt',None),
        ('addedBrandName',None),
        ('brand_id',0),
        ('brand_name',None),
        ('suppliers_id',0),
        ('shop_price', 3999),
        ('exclusive', -1),
        ('user_price[]', -1),
        ('user_rank[]', 1),
        ('user_price[]', -1),
        ('user_rank[]', 2),
        ('user_price[]', -1),
        ('user_rank[]', 3),
        ('user_price[]', -1),
        ('user_rank[]', 4),
        ('volume_number[]',None),
        ('volume_price[]',None),
        ('market_price', '4798.8'),
        ('give_integral', -1),
        ('rank_integral', -1),
        ('buymax_start_date',None),
        ('buymax_end_date',None),
        ('cost_price', 0),
        ('goods_img_url', '商品图片外部URL'),
        ('auto_thumb', 1),
        ('goods_desc', None),
        ('goods_weight',None),
        ('weight_unit', 1),
        ('goods_number', 1),
        ('warn_number', 1),
        ('ghost_count',None),
        ('is_on_sale',1),
        ('is_alone_sale', 1),
        ('keywords',None),
        ('goods_brief',None),
        ('seller_note',None),
        ('goods_type',0),
        ('cat_id1', 0),
        ('brand_id1', 0),
        ('keyword1',None),
        ('is_single',1),
        ('cat_id2', 0),
        ('brand_id2', 0),
        ('keyword2',None),
        ('price2',None),
        ('article_title',None),
        ('goods_id',0),
        ('act', 'insert')
         ]
    files = {'goods_img': ('abc.jpg', open('abc.jpg', 'rb'), 'image/jpeg')}
    res = requests.post(url, headers=headers, data=data, files=files)
    print(res.text)
    assert '添加商品成功' in res.text


post_04()



