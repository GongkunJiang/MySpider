# coding=utf-8
# 使用了线程库
from threading import Thread
# 队列
from selenium.webdriver import PhantomJS, ActionChains
import time
import re
import requests
import os


def start(n,comic_url):
    urllists.append(comic_url)
    driver = PhantomJS()
    driver.get(comic_url)
    get_images_url(n, driver)
    while True:
        try:
            driver.find_element_by_xpath("//li[@id='next_item']/a[@id='mainControlNext']").click()
            comic_url = driver.current_url
            if comic_url not in urllists:
                urllists.append(comic_url)
                get_images_url(n,driver)
                driver.find_element_by_xpath("//li[@id='next_item']/a[@id='mainControlNext']").click()
                # print n + '\t' + comic_url

        except:
            print 'All done!'
            break


def get_images_url(n,driver):
    pages = driver.find_elements_by_xpath("//span[contains(@class,'comic-ft')]")
    # 图片需滑动页面还需要一点时间才能加载出来
    for page in pages:
        ActionChains(driver).move_to_element(page).perform()
        # 容易受到实时网速影响，爬的过程中可能需要动态调整
        time.sleep(0.25)
    response = driver.page_source.encode('utf-8')
    title = driver.find_element_by_xpath('//span[@class="title-comicHeading"]').get_attribute('textContent')
    chapter = title.replace(' ', '_').replace('10:00',u'10点')
    print n + '\t' + title
    # xpath抓不到图片地址 find_element_by_xpath("//li[contains(@style,'width: 313px')]/img")
    # 只好用正则
    with open('./assets/34_OnePiece.html', 'w') as f:
        f.write(response)
    pattern = re.compile('<img src="(https://manhua.qpic.cn/manhua_detail/0/.*.jpg/0)')
    images_url = re.findall(pattern, response)
    for m in range(0, len(pages)):
        # print n + '\t' + pages[m].text, images_url[m]
        store_images(n,chapter, pages[m].text, images_url[m])


def store_images(n,chapter, page, url):
    Image_name = get_name(page)
    Image_data = requests.Session().get(url, headers={"User-Agent": "Mozilla/5.0"}).content
    filepath = './assets/OnePiece/%s' % chapter
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open('%s/%s.jpg' % (filepath, Image_name), 'wb') as f:
        f.write(Image_data)
    # print n + '\tSave done\t' + chapter + page


def get_name(page):
    num = page.split('/')[0]
    if int(num) < 10:
        return '0' + num
    else:
        return num
urllists = []
if __name__ == '__main__':
    comic_url = "http://ac.qq.com/ComicView/index/id/505430/cid/"

    # 构建线程
    threads = []
    for n in range(0, 5):
        t = Thread(target=start, args=('No.' + str(n + 1), comic_url + str(n+1) + '?fromPrev=1'))
        threads.append(t)
        # 启动所有线程
    for thr in threads:
        thr.start()





























