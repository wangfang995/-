#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wf'
__mtime__ = '2019/7/25'
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

from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf

#接口串联
# 1、在文件最上边创建一个空字典
# 2、把接口响应中的数据取出来，存到这个空字典中
# 3、下个接口可以从这个字典中根据key取值

# 往请求头添加数据
# 1、创建一个字典，把需要添加的数据存入字典中
# 2、请求方法中使用headers=来传入请求头数据


#请求数据在请求地址里边
# 1、使用.format进行字符串格式化

# 1. 注册

data ={}
@allure.feature("后台用户管理流程")
@allure.story("注册新用户")
def test_user_admin_register_1():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'
    username = "wf" + random_tool.random_str_abc(4)
    req = {"email":"985092749@qq.com","icon":"","nickName":"xuepl","note":"","password":"123456","username":username}
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户名，实际结果:{},预期结果:{}".format(body['data']["username"], username)):
        pass
    assert_tool.assert_equal(body['data']["username"], username)
    data ["id"] = body['data']["id"]
    data ["username"] =body['data']["username"]


# 2.给用户分配角色
@allure.feature("后台用户管理流程")
@allure.story("给用户分配角色 1,商品管理员。 2，商品分类管理员。 3，商品类型管理员。 4，品牌管理员 ")
def test_user_admin_role_update():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +"/admin/role/update"
    req = {
        "adminId": data ["id"],
        "roleIds": [1,2,3,4]
    }
    resp = request_tool.post_request(url, data=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户角色，实际结果:{},预期结果:{}".format(body['data'],4)):
        pass
    assert_tool.assert_equal(body['data'],4)

# 3.查询用户角色
@allure.feature("后台用户管理流程")
@allure.story("查询用户角色")
def test_user_admin_pwd():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +"/admin/role/{}".format(data ["id"])
    resp = request_tool.get_request(url)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户角色名称，实际结果:{},预期结果:{}".format(body["data"][0]["name"],"商品管理员")):
        pass
    assert_tool.assert_equal(body["data"][0]["name"], "商品管理员")


# 4.登录
@allure.feature("后台用户管理流程")
@allure.story("登录")
def test_user_admin_login():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +"/admin/login"

    req ={
  "password": "123456",
  "username": data["username"]
}
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body["data"][ "tokenHead"],"Bearer ")
    data["token"] = body["data"][ "tokenHead"]+body["data"]["token"]

# 5.获取当前登录用户信息
@allure.feature("后台用户管理流程")
@allure.story("获取当前登录用户信息")
def test_info():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url =  conf.GY_API_URL +"/admin/info"
    headers = {
            'Authorization':data["token"]
    }
    resp = request_tool.get_request(url,headers=headers)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body["data"]["username"], data ["username"])


# 6.删除指定用户信息
@allure.feature("后台用户管理流程")
@allure.story("删除指定用户信息")
def test_delete():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url =  conf.GY_API_URL +"/admin/delete/{}".format(data ["id"])
    resp = request_tool.post_request(url)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body["data"])




