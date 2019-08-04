#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wf'
__mtime__ = '2019/7/26'
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
import json

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
data = excel_tool.get_test_case('data/demo/add_product_category.xls')
@pytest.mark.parametrize('uri,datas,code',data[1],ids=data[0])
@pytest.fixture("添加商品分类")
def test_change_pwd_var (token,uri,datas,code):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + uri
    req = json.loads(datas)
    headers = {
        'Authorization': token,
        'charset': 'UTF-8'
    }
    resp = request_tool.post_request(url, json=req, headers=headers)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果:{},预期结果:200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言code，实际结果:{},预期结果:{}".format(body['code'],code)):
        pass
    assert_tool.assert_equal(body['code'], code)

