from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.lqr.wechat"
caps["appActivity"] = "com.lqr.wechat.ui.activity.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()

driver.quit()



