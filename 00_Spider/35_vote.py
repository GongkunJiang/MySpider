from selenium.webdriver import PhantomJS

driver = PhantomJS(executable_path=r'E:\Documents\Apps\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://cxwh.kexing100.com:82/?app_act=detail&id=328&from=groupmessage'
driver.get(url)
while True:
    driver.refresh()
    print driver.find_element_by_xpath("//div[@class='xinfo']").text
    # driver.execute_script("return localStorage.setItem('toupiao','0')")
    driver.execute_script("return localStorage.removeItem('toupiao')")
    driver.delete_all_cookies()
    driver.refresh()
    vote = driver.find_element_by_xpath("//span/input[@class='btn1']").click()
    # break
