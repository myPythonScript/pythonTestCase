from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62025",
    "appPackage": "cn.kmob.screenfingermovelock",
    "appActivity": "com.samsung.ui.FlashActivity",
	"automationName": "uiautomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("cn.kmob.screenfingermovelock:id/lockerCheckBox").click()
sleep(1)
TouchAction(driver).press(x=120, y=180).move_to(x=350, y=180).move_to(x=600, y=180).move_to(x=350, y=410).move_to(x=120, y=650).move_to(x=360, y=650).move_to(x=600, y=650).release().perform()
sleep(2)
driver.find_element_by_xpath("//*[@text='继续']").click()
sleep(2)
exist = driver.find_elements_by_xpath("//*[@text='先玩玩看']")
if len(exist) != 0:
    exist[0].click()
    driver.quit()
else:
    TouchAction(driver).press(x=120, y=180).move_to(x=350, y=180).move_to(x=600, y=180).move_to(x=350, y=410).move_to(x=120, y=650).move_to(x=360, y=650).move_to(x=600, y=650).release().perform()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='确认']").click()
    sleep(2)
    print(driver.find_element_by_id("cn.kmob.screenfingermovelock:id/lockerCheckBox").is_selected())
    # assert driver.find_element_by_id("cn.kmob.screenfingermovelock:id/lockerCheckBox").is_selected() == True
