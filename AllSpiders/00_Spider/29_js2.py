# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

# 向下滚动10000像素
js = "document.body.scrollTop=10000"
#js="var q=document.documentElement.scrollTop=10000"
time.sleep(3)

#查看页面快照
driver.save_screenshot("29_js2a.png")

# 执行JS语句
driver.execute_script(js)
time.sleep(10)

#查看页面快照
driver.save_screenshot("29_js2b.png")

driver.quit()