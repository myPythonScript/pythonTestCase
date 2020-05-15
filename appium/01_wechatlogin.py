from appium import webdriver
from time import sleep

caps = {
	"platformName": "Android",
	["platVersion"]: "5.1.1",
	["deviceName"]: "127.0.0.1:62001",
	["appPackage"]: "com.lqr.wechat",
	["appActivity"]: "com.lqr.wechat.ui.activity.SplashActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.find_element_by_xpath("//[@text='登录']").click()
sleep(1)
driver.find_element_by_xpath()
