#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wf'
__mtime__ = '2019/7/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

#发送请求的包名 requests
#安装包
#导入
import requests
#json 格式数据
a = {
  "password": "123456",
  "username": "admin"
}
b = requests.post("http://qa.yansl.com:8080/admin/login",json =a)
print(b.text)

#键值对格式数据
c = {"adminId":32,"roleIds":(1,2,3)}
d = requests.post("http://qa.yansl.com:8080/admin/role/update",data=c)
print(d.text)

#get请求，键值对格式数据
e = {"name":"谭小冬","pageSize":5,"pageNum":1}
f = requests.get("http://qa.yansl.com:8080/admin/list",params=e)
print(f.text)

g ={"orderSn":22,"receiverKeyword":22,"status":22,"orderType":22,"sourceType":22,"createTime":22,"pageSize":22,"pageNum":22}
h = requests.get("http://qa.yansl.com:8080/order/list",params=g)
print(h.text)