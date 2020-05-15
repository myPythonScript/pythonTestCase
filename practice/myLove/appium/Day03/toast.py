from appium import webdriver
from time import sleep
caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity",
    "automationName": "uiautomator2",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.find_element_by_id('com.lqr.wechat:id/btnLogin').click()
sleep(2)
driver.find_element_by_id("com.lqr.wechat:id/etPhone").send_keys("18010181267")
driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123")
driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()
sleep(1)
results = driver.find_elements_by_xpath('//*[@text="登录失败1001"]')
if results:
    print("定位到了toast")
    print(results[0].text)
else:
    print("未定位到toast")

