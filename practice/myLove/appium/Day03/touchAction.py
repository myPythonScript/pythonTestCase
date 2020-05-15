from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "cn.kmob.screenfingermovelock",
    "appActivity": "com.samsung.ui.FlashActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.find_element_by_id("cn.kmob.screenfingermovelock:id/patternTxt").click()
TouchAction(driver).press(x=117,y=170).move_to(x=117,y=421).wait(300).\
	move_to(x=117,y=647).wait(300).\
	move_to(x=357,y=410).wait(300).\
	move_to(x=357,y=410).wait(300).\
	move_to(x=594,y=173).\
	release().perform()
driver.quit()