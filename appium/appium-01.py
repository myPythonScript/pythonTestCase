from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "06157df6ad37300f",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity"
}

driver = webdriver.Remote("http//:127.0.0.1:4273/wd/hub", caps)

driver.quit()
