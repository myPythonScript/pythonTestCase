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
login_btn = driver.find_elements_by_id("com.lqr.wechat:id/btnLogin")
sleep(1)
if len(login_btn) != 0:
    print(login_btn[0].get_attribute("resourceId"))
    print(login_btn[0].get_attribute("text"))
    print(login_btn[0].get_attribute("className"))
    print(login_btn[0].text)
    print(login_btn[0].size)
    print(login_btn[0].location)

    login_btn[0].click()
    driver.find_element_by_xpath("//*[@text='你的手机号码']").send_keys("18010181267")
    driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123456")
    driver.find_element_by_xpath("//*[@text='登录']").click()
    sleep(2)
    assert "android.widget.TextView" in driver.page_source
else:
    address_list = driver.find_element_by_class_name("android.widget.TextView")
    print(address_list.get_attribute("resourceId"))
    print(address_list.get_attribute("text"))
    print(address_list.get_attribute("className"))

