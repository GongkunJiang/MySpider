# coding=utf-8
from bs4 import BeautifulSoup
import time,urllib2
from urllib import urlretrieve
import subprocess
from selenium import webdriver
from selenium.webdriver import ActionChains
#创建新的Selenium driver
driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# 用Selenium试试Firefox浏览器:
# driver = webdriver.Firefox()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# 单击图书预览按钮 driver.find_element_by_id("sitbLogoImg").click() imageList = set()
# 等待页面加载完成
time.sleep(10)
driver.save_screenshot('31_web1.png')
# 当向右箭头可以点击时,开始翻页
imageList = []
j = 1
# currentpage = driver.find_elements_by_xpath('//span/span[@class="a-carousel-page-current"]')[0].get_attribute('textContent')
maxpages = driver.find_elements_by_xpath('//span/span[@class="a-carousel-page-max"]')
# print currentpage
for page in maxpages:
    print page.get_attribute('textContent')

driver.quit()
# for i in range(1,19):
#     # driver.find_element_by_class_name("a-button a-button-image a-carousel-button a-carousel-goto-nextpage").click()
#     ac = driver.find_element_by_id("a-autoid-7")
#     ActionChains(driver).move_to_element(ac).click(ac).perform()
#     # time.sleep(2)
#     # 获取已加载的新页面(一次可以加载多个页面,但是重复的页面不能加载到集合中)
#     pages = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-mini']/img")
#
#     for page in pages:
#         image = page.get_attribute("src")
#         print  "No.%d\t"%j + image
#         # downloade = urllib2.urlopen(image).read()
#         # with open("./images/%d.jpg" % j,'wb') as f:
#         #     f.write(downloade)
#         # urlretrieve(image, "./images/%d.jpg" % j)
#         # print "已下载%d.jpg" % j
#         j += 1
#         imageList.append(image)
# driver.save_screenshot('31_web2.png')
# driver.quit()
#
# # 用Tesseract处理我们收集的图片URL链接
# k = 1
# for image in sorted(imageList):
#     # 保存图片
#     urlretrieve(image, "./images/%d.jpg"%k)
#     print "已下载%d.jpg" %k
#     k += 1
#     # p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     # f = open("page.txt", "r")
#     # p.wait()
#     # print(f.read())