#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wf'
__mtime__ = '2019/7/31'
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
from time import sleep

import allure
from tools import assert_tool
@allure.feature("添加商品流程")
@allure.story("登录")
def test_logen(base):
    #打开登录界面http://qa.yansl.com/#/login
    base.get("打开登录界面","http://qa.yansl.com/#/login")
    #输入用户名//input[@name="username"]
    base.send_keys("输入用户名","""//input[@name="username"]""","admin")
    #输入密码//input[@name="password"]
    base.send_keys("输入密码","""//input[@name="password"]""","123456")
    #点击登录//span[contains(text(),'登录')]
    base.click("点击登录","""//span[contains(text(),'登录')]""")
    try:
        #点击残忍拒绝//span[text()='残忍拒绝']
        base.click("点击残忍拒绝","""//span[text()='残忍拒绝']""")
        #点击登录//span[contains(text(),'登录')]
        base.click("点击登录", """//span[contains(text(),'登录')]""")
    except:
        pass
    #断言 页面跳转至首页//a[contains(text(),"首页")]
    # f = False
    # try:
    #     base.local_element("""//span[contains(text(),"首页")]""")
    #     f = True
    # except:
    #     pass
    # assert_tool.assert_equal(f,True)
    # with allure.step("登录断言，实际结果{}，预期结果{}".format(f,"True")):pass

    page_source = base.driver.page_source
    with allure.step("登录页面跳转"):
        allure.attach(page_source,"实际结果",allure.attachment_type.TEXT)
        allure.attach("首页", "预期结果", allure.attachment_type.TEXT)
    assert_tool.assert_in( page_source,"首页")

@allure.feature("添加商品流程")
@allure.story("添加商品信息")
def test_add(base):
    #点击商品(//span[@slot="title"])[1]
    base.click("点击商品","""(//span[@slot="title"])[1]""")
    #点击添加商品//span[contains(text(),"添加商品")]
    base.click("点击添加商品","""//span[contains(text(),"添加商品")]""")
    #点击商品分类//span[@class="el-cascader__label"]
    base.click("点击商品分类","""//span[@class="el-cascader__label"]""")
    #点击服装//li[contains(text(),"服装")]
    base.click("点击服装","""//li[contains(text(),"服装")]""")
    #点击外套//li[contains(text(),"外套")]
    base.click("点击外套","""//li[contains(text(),"外套")]""")
    #添加商品名称//label[text()='商品名称：']/../div//input
    base.send_keys("添加商品名称","""//label[text()='商品名称：']/../div//input""","cwfreg")
    #添加副标题//label[text()='副标题：']/../div//input
    base.send_keys("添加副标题","""//label[text()='副标题：']/../div//input""","fewopgjrerkh")
    #点击选择品牌//input[@placeholder="请选择品牌"]
    base.click("点击选择品牌","""//input[@placeholder="请选择品牌"]""")
    #点击小米//span[(text()='小米')]
    base.click("点击小米","""//span[(text()='小米')]""")
    #请输入内容//textarea[@placeholder="请输入内容"]
    base.send_keys("请输入内容","""//textarea[@placeholder="请输入内容"]""","红烧肉")
    #点击下一步，填写商品促销//span[text()="下一步，填写商品属性"]
    base.click("点击下一步，填写商品促销","""//span[text()="下一步，填写商品促销"]""")
    # 点击下一步，填写商品属性//span[text()="下一步，填写商品属性"]
    sleep(1)
    base.click("点击下一步，填写商品属性", """//span[text()="下一步，填写商品属性"]""")
    # #点击电脑详情页//div[text()="电脑端详情"]
    # base.click("点击电脑详情页", """//div[text()="电脑端详情"]""")
    # #切入iframe(//iframe)[1]
    # base.switch_to_frame("切入iframe","""(//iframe)[1]""")
    # #s输入内容//body
    # base.send_keys("输入内容","""//body""","红烧肉")
    # #切出iframe
    # base.switch_to_content("切出iframe")
    # 点击下一步，选择商品关联//span[text()="下一步，选择商品关联"]
    base.click("点击下一步，选择商品关联", """//span[text()="下一步，选择商品关联"]""")
    sleep(1)
    # 点击完成，提交商品//span[text()="完成，提交商品"]
    base.click("点击下一步，填写商品关联", """//span[text()="完成，提交商品"]""")
    sleep(1)
    # 点击确定//span[contains(text(),"确定")]
    base.click("点击确定","""//span[contains(text(),"确定")]""")
