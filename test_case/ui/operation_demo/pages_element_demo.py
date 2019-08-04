from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config.conf import DRIVER_PATH



driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器大小
driver.maximize_window()


def get_url():
    driver.get("D:\\softwareData\\Python\\gy-api-wf\\demo(1).html")
def quit_browser():
    driver.quit()
def test_demo():
    #定位元素//input[@type= "text"]
    text=driver.find_element_by_xpath('//input[@type= "text"]')
    # 清空
    text.clear()
    # 输入
    text.send_keys("我想吃烧烤")
    #获取属性的值
    # print (text.get_attribute("value"))
    print( )
def file_demo():
    #定位元素
    file=driver.find_element_by_xpath('//input[@type= "file"]')
    # 清空
    file.clear()
    # 输入
    file.send_keys("D:\8718367adab44aed6bab487db41c8701a08bfb46.gif")

def radio_demo():
    #定位元素
    radio1=driver.find_element_by_xpath('(//input[@type= "radio"])[1]')
    radio1.click()
    radio2 = driver.find_element_by_xpath('(//input[@type= "radio"])[2]')
    radio2.click()

def checkbox_demo():
    #定位元素
    radio3=driver.find_element_by_xpath('(//input[@type="checkbox"])[1]')
    radio3.click()
    radio4=driver.find_element_by_xpath('(//input[@type="checkbox"])[2]')
    radio4.click()
    # radio5 = driver.find_element_by_xpath('(//input[@type="checkbox"])[3]')
    # radio5.click()

def button_demo():
    #定位元素
    button=driver.find_element_by_xpath('(//input[@type="button"]')
    button.click()

def password_demo():
    #定位元素//input[@type= "text"]
    password=driver.find_element_by_xpath('//input[@type="password"]')
    # 清空
    password.clear()
    # 输入
    password.send_keys("efwereg")

def number_demo():
    #定位元素//input[@type= "text"]
    number=driver.find_element_by_xpath('//input[@type="number"]')
    # 清空
    number.clear()
    # 输入
    number.send_keys(123456)

def date_demo():
    js1 = """var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");"""
    driver.execute_script(js1)

def time_demo():
    js2 = """var xpath = '//input[@type="time"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","12:12");"""
    driver.execute_script(js2)

def textarea_demo():
    textarea=driver.find_element_by_xpath('//textarea')
    # 清空
    textarea.clear()
    # 输入
    textarea.send_keys('二大娘')

def select_demo():
    # select=driver.find_element_by_xpath('//select/option[1]')
    # select.click()
    b=driver.find_element_by_xpath('//select')
    b1=Select(b)
    b1.select_by_index(0)
    sleep(2)
    b1.select_by_value("z2")
    sleep(2)
    b1.select_by_visible_text("周龙3")

def a_demo():
    # a = driver.find_element_by_link_text("当当")
    # a.click()
    c=driver.find_element_by_partial_link_text("度娘")
    d=ActionChains(driver)
    d.key_down(Keys.CONTROL).click(c).key_up(Keys.CONTROL).perform()


if __name__ == '__main__':
    get_url()
    sleep(2)
    # test_demo()
    # sleep(2)
    # file_demo()
    # sleep(2)
    # radio_demo()
    # sleep(2)
    # checkbox_demo()
    # sleep(2)
    # # button_demo()
    # # sleep(2)
    # password_demo()
    # sleep(2)
    # number_demo()
    # sleep(2)
    # date_demo()
    # sleep(2)
    # time_demo()
    # sleep(2)
    textarea_demo()
    sleep(2)
    select_demo()
    sleep(2)
    a_demo()
    sleep(2)
    quit_browser()




