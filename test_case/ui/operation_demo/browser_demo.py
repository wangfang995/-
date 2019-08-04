# 打开浏览器
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

driver = webdriver.Chrome(DRIVER_PATH)
# 最大化浏览器窗口
driver.maximize_window()
# driver.set_window_size(1280,900) #自定义，不建议
# 打开网址
driver.get(GY_WEB_URL)
driver.get("https://www.baidu.com")
sleep(1)
driver.get("https://www.jd.com")

# 后退
driver.back()
sleep(1)
# 前进
driver.forward()
sleep(1)
# 刷新
driver.refresh()


# 延时驱动
sleep(2)
# 关闭浏览器
# driver.close()
# # 关闭驱动
driver.quit()
# 调整浏览器大小