# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests


def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)
    text = raw_input("请输入验证码：")
    # 返回用户输入的验证码
    return text


def zhihuLogin():
    # 构建一个Session对象，可以保存页面Cookie
    sess = requests.Session()

    # 请求报头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 首先获取登录页面，找到需要POST的数据（_xsrf)，同时会记录当前网页的Cookie值
    html = sess.get("https://passport.fang.com/register.aspx", headers=headers).text
    # 调用lxml解析库
    bs = BeautifulSoup(html, "lxml")


    captcha_url = bs.select('div img[id="imgcode"]')[0].attrs['src']
    # 发送图片的请求，获取图片数据流，
    captcha_data = sess.get(captcha_url, headers=headers).content
    # 获取验证码里的文字，需要手动输入
    text = captcha(captcha_data)

    data = {
        "email": "123636274@qq.com",
        "password": "ALARMCHIME",
        "captcha": text
    }

    # 发送登录需要的POST数据，获取登录后的Cookie(保存在sess里)
    response = sess.post("https://www.zhihu.com/login/email", data=data, headers=headers)
    # print response.text

    # 用已有登录状态的Cookie发送请求，获取目标页面源码
    response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers=headers)
    with open("my.html", "w") as f:
        f.write(response.text.encode("utf-8"))


if __name__ == "__main__":
    zhihuLogin()
