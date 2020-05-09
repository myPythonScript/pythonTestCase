from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

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
    print("登录")
    login_btn[0].click()
    driver.find_element_by_xpath("//*[@text='你的手机号码']").send_keys("18010181267")
    driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123456")
    driver.find_element_by_xpath("//*[@text='登录']").click()
    sleep(2)
    assert "android.widget.TextView" in driver.page_source
else:
    print("已登录")

# # 微信界面右上角的“+”按钮
# add_element = driver.find_element("id", "com.lqr.wechat:id/ibAddMenu")
# add_element.click()
# driver.find_element("xpath", "//*[@text='帮助与反馈']").click()
# driver.implicitly_wait(10)
# assert len(driver.find_elements("xpath", "//*[@text='热点问题']")) != 0
# driver.find_element_by_id("com.lqr.wechat:id/ivToolbarNavigation").click()


WebDriverWait(driver, 20).until(presence_of_element_located(("id", "com.lqr.wechat:id/ibAddMenu")))
driver.find_element("id", "com.lqr.wechat:id/ibAddMenu").click()
driver.find_element("xpath", "//*[@text='扫一扫']").click()
driver.implicitly_wait(20)
assert len(driver.find_elements("xpath", "//*[@text='二级码/条码']")) != 0
driver.tap([(40, 100)])
