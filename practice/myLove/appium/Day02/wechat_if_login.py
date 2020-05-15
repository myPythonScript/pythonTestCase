from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity",
    "noReset": True
    # "unicodeKeyboard": True,
    # "resetKeyboard": True,
    # "automationName": "uiautomator2",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

results = driver.find_elements_by_id("com.lqr.wechat:id/btnLogin")

if results:
    print("存在登录按钮，未登录")
    results[0].click()
    driver.find_element_by_id("com.lqr.wechat:id/etPhone").send_keys("18010181267")
    driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123456")
    login_btn = driver.find_element_by_id("com.lqr.wechat:id/btnLogin")
    if login_btn.get_attribute("enabled"):
        print("可用")
        login_btn.click()
    else:
        print("不可用")
else:
    print("不存在登录按钮, 已登录")

# 查找通讯录并输出属性
contacts = driver.find_element_by_id("com.lqr.wechat:id/tvContactsTextPress")
print(contacts.get_attribute('resourceId'))
print(contacts.get_attribute('className'))
print(contacts.get_attribute('displayed'))

driver.quit()
