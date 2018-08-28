# coding=utf-8

from selenium import webdriver
import time,requests


driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.douban.com")
driver.save_screenshot("25_douban0.png")
code_url = driver.find_element_by_xpath('//div[@class="item item-captcha"]/img').get_attribute('src')
code_data = requests.Session().get(code_url,headers = {"User-Agent" : "Mozilla/5.0"}).content
with open("25db_code.jpg", "wb") as f:
    f.write(code_data)
code = raw_input("请输入验证码：")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("18179043235")
driver.find_element_by_name("form_password").send_keys("jgk888666")
driver.find_element_by_name("captcha-solution").send_keys(code)
# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()
driver.save_screenshot("25_douban1.png")
# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("25_douban2.png")

with open("25_douban.html", "w") as file:
    file.write(driver.page_source.encode('utf-8'))

driver.quit()