# coding=utf-8

from selenium.webdriver import PhantomJS, ActionChains
import time
import re
import requests
import os


def start(comic_url):
    driver.get(comic_url)
    get_images_url()
    while True:
        try:
            driver.find_element_by_xpath("//li[@id='next_item']/a[@id='mainControlNext']").click()
            print driver.current_url
            get_images_url()
        except:
            print 'All done!'
            break


def get_images_url():
    pages = driver.find_elements_by_xpath("//span[contains(@class,'comic-ft')]")
    # 图片需滑动页面还需要一点时间才能加载出来
    for page in pages:
        ActionChains(driver).move_to_element(page).perform()
        # 容易受到实时网速影响，爬的过程中可能需要动态调整
        time.sleep(0.25)
    response = driver.page_source.encode('utf-8')
    title = driver.find_element_by_xpath('//span[@class="title-comicHeading"]').get_attribute('textContent')
    chapter = title.replace(' ', '_').replace('10:00',u'10点')
    print title
    # xpath抓不到图片地址 find_element_by_xpath("//li[contains(@style,'width: 313px')]/img")
    # 只好用正则
    with open('./assets/34_OnePiece.html', 'w') as f:
        f.write(response)
    pattern = re.compile('<img src="(https://manhua.qpic.cn/manhua_detail/0/.*.jpg/0)')
    images_url = re.findall(pattern, response)
    for n in range(0, len(pages)):
        print pages[n].text, images_url[n]
        store_images(chapter, pages[n].text, images_url[n])


def store_images(chapter, page, url):
    Image_name = get_name(page)
    Image_data = requests.Session().get(url, headers={"User-Agent": "Mozilla/5.0"}).content
    filepath = './assets/OnePiece/%s' % chapter
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open('%s/%s.jpg' % (filepath, Image_name), 'wb') as f:
        f.write(Image_data)
    print 'Save done\t' + chapter + page


def get_name(page):
    num = page.split('/')[0]
    if int(num) < 10:
        return '0' + num
    else:
        return num


if __name__ == '__main__':
    driver = PhantomJS()
    comic_url = "http://ac.qq.com/ComicView/index/id/505430/cid/920"
    start(comic_url)
    driver.close()





























