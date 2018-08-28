# coding=utf-8
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("https://www.baidu.com/")
driver.save_screenshot("28_js0.png")
# 给搜索输入框标红的javascript脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红js脚本
driver.execute_script(js)

#查看页面快照
driver.save_screenshot("28_js1.png")

#js隐藏元素，将获取的图片元素隐藏
img = driver.find_element_by_xpath("//*[@id='lg']/img")
driver.execute_script('$(arguments[0]).fadeOut()',img)
driver.save_screenshot("28_js2.png")
# 向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

#查看页面快照
driver.save_screenshot("28_js3.png")

driver.quit()