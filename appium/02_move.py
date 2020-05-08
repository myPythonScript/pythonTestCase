from appium import webdriver
from time import sleep

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "app": "C:/Users/Administrator/Desktop/app-debug.apk",
    "autoLaunch": False
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


def login():
    driver.launch_app()
    driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()
    sleep(1)

    driver.find_element_by_xpath("//*[@text='你的手机号码']").send_keys("18010181267")
    driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("123456")
    driver.find_element_by_xpath("//*[@text='登录']").click()
    sleep(5)
    size = driver.get_window_size()
    print("size:" % size)
    x1, x2 = size["width"] * 0.9, size["width"] * 0.1
    y1, y2 = size["height"] / 2, size["height"] / 2
    print(x1, y1, x2, y2)
    driver.swipe(x1, y1, x2, y2, duration=2000)
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\123.png")
    assert "android.widget.TextView" in driver.page_source


isInstall = driver.is_app_installed("com.lqr.wechat")
if isInstall is True:
    print("已安装")
    login()
else:
    print("未安装")
    driver.install_app(r"C:\Users\Administrator\Desktop\app-debug.apk")
    print("安装完成")
    login()
