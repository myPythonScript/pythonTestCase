from appium import webdriver
from time import sleep

# caps = {
#     "platformName": "Android",
#     "platformVersion": "7.0",
#     "deviceName": "06157df6ad37300f",
#     "appPackage": "com.lqr.wechat",
#     "appActivity": "com.lqr.wechat.ui.activity.SplashActivity"
# }

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity",
    "noReset": "True"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()
sleep(1)

driver.find_element_by_xpath("//*[@text='你的手机号码']").send_keys("18010181267")
driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123456")
driver.find_element_by_xpath("//*[@text='登录']").click()
sleep(2)
assert "android.widget.TextView" in driver.page_source
