from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "06157df6ad37300f",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity"
}

# caps = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.lqr.wechat",
#     "appActivity": "com.lqr.wechat.ui.activity.SplashActivity"
# }

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
