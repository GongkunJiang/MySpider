# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("18179043235")
driver.find_element_by_name("form_password").send_keys("jgk888666")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("douban.png")

with open("douban.html", "w") as file:
    file.write(driver.page_source.encode('utf-8'))

driver.quit()