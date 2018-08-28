# coding=utf-8
from selenium import webdriver
from PIL import Image
import time,requests
driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://passport.17173.com/register')
driver.find_element_by_xpath("//li[@class='reg-tab-nav']").click()
driver.find_element_by_name("mobile").send_keys(str(input("请输入手机号：")))
driver.find_element_by_id("pw").send_keys("abc123")
driver.find_element_by_xpath("//div[@class='fbox-main clearfix zg-code-box']/button").click()
code_url = 'https://passport.17173.com/register/captcha'
code_data = requests.Session().get(code_url,headers = {"User-Agent" : "Mozilla/5.0"}).content
with open("26ph_code.jpg", "wb") as f:
    f.write(code_data)
time.sleep(1)
driver.save_screenshot("26_phone1.png")
Image.open('26_phone1.png').show()
code = raw_input("请输入验证码：")
driver.find_element_by_class_name("form-text").send_keys(code)
driver.find_element_by_xpath("//button[@id='submit_validate_code']").click()
time.sleep(1)
driver.save_screenshot("26_phone2.png")
driver.quit()