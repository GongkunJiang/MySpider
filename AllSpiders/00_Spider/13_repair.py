# -*- coding:utf-8 -*-

import urllib
import urllib2
from lxml import etree


def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
    """
    #print url
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"}
    #
    # request = urllib2.Request(url,headers=headers)
    # html = urllib2.urlopen(request).read()
    # # 解析HTML文档为HTML DOM模型
    # content = etree.HTML(html)
    # # print content
    # # 返回所有匹配成功的列表集合
    # link_list = content.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    #
    # #link_list = content.xpath('//a[@class="j_th_tit"]/@href')
    # for link in link_list:
    #     print link
    #     fulllink = "http://tieba.baidu.com" + link
    #     # 组合为每个帖子的链接
    #     print fulllink
    #     # loadImage(fulllink)
    req = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(req).read()

    # 解析html 为 HTML 文档
    selector = etree.HTML(html)

    # 抓取当前页面的所有帖子的url的后半部分，也就是帖子编号
    # http://tieba.baidu.com/p/4884069807里的 “p/4884069807”
    links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

    # links 类型为 etreeElementString 列表
    # 遍历列表，并且合并成一个帖子地址，调用 图片处理函数 loadImage
    for link in links:
        link = "http://tieba.baidu.com" + link
        # print link
        loadImage(link)


# 取出每个帖子里的每个图片连接
def loadImage(link):
    # headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"}
    request = urllib2.Request(link, headers = headers)
    html = urllib2.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出帖子里每层层主发送的图片连接集合
    #link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    #link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # 取出每个图片的连接
    for link in link_list:
        print link
        writeImage(link)


def writeImage(link):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    #print "正在保存 " + filename
    # headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"}
    # 文件写入
    request = urllib2.Request(link, headers = headers)
    # 图片原始数据
    image = urllib2.urlopen(request).read()
    # 取出连接后10位做为文件名
    filename = link[-40:]
    # 写入到本地磁盘文件内
    # with open(filename, "wb") as f:
    with open('./images/' + filename + '.png', 'wb') as f:
        f.write(image)
    print "已经成功下载 "+ filename

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        #filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        loadPage(fullurl)
        #print html

    print "谢谢使用"

if __name__ == "__main__":
    # kw = raw_input("请输入需要爬取的贴吧名:")
    # beginPage = int(raw_input("请输入起始页："))
    # endPage = int(raw_input("请输入结束页："))
    kw = "美女"
    beginPage = 1
    endPage = 3
    headers = {"User-Agent": "Mozilla/4.0"}
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    # print fullurl
    tiebaSpider(fullurl, beginPage, endPage)





