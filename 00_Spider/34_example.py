# -*- coding:utf-8 -*-

from selenium import webdriver
import sys
from time import sleep
from threading import Thread


def test_baidu_search(n,url):
    driver = webdriver.PhantomJS()

    print n + u"\t开始[case_0001]百度搜索"
    driver.get(url)

    print n + u"\t清除搜索中数据，输入搜索关键词"
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(u"开源优测")

    print n + u"\t单击 百度一下 按钮 开始搜索"
    driver.find_element_by_id("su").click()
    sleep(3)

    print n + u"\t关闭浏览器，退出webdriver"
    driver.quit()


if __name__ == "__main__":
    # 浏览器和首页url
    url = 'http://www.baidu.com'

    # 构建线程
    threads = []
    for n in range(0,5):
        t = Thread(target=test_baidu_search, args=(str(n+1),url))
        threads.append(t)
        # 启动所有线程
    for thr in threads:
        thr.start()
