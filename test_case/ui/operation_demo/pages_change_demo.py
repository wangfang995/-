from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器大小
driver.maximize_window()


def get_url():
    driver.get("D:\\softwareData\\Python\\gy-api-wf\\demo(1).html")


def quit_browser():
    driver.quit()

def open_a():
    baidu=driver.find_element_by_partial_link_text("度娘")
    jd=driver.find_element_by_partial_link_text("京东")
    dd=driver.find_element_by_partial_link_text("当当")
    d = ActionChains(driver)
    d.key_down(Keys.CONTROL).click(baidu).click(jd).click(dd).key_up(Keys.CONTROL).perform()
    sleep(5)

def window_change_demo():
    handles=driver.window_handles
    for b in handles:
        driver.switch_to.window(b)
        sleep(2)
        if (driver.title.__contains__('百度')):
            break


def open_alert():
    #点击重置按钮
    driver.find_element_by_xpath('//input[@type="reset"]').click()
    sleep(2)
def alert_alert():
    #切换到弹框
    c=driver.switch_to.alert
    #确认
    c.accept()

def open_alert2():
    #点击重置按钮
    driver.find_element_by_xpath('//input[@type="button"]').click()
    sleep(2)
def alert_alert2():
    #切换到弹框
    d=driver.switch_to.alert
    # d.send_keys("hello")
    d.dismiss("hello")

if __name__ == '__main__':
    get_url()
    sleep(2)
    # open_a()
    # window_change_demo()
    open_alert()
    sleep(2)
    alert_alert()
    sleep(2)
    open_alert2()
    sleep(2)
    quit_browser()









