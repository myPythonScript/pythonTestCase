from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction


caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = 'com.android.androidui'
caps['appActivity'] = '.MainActivity'
caps['uiautomator'] = 'Uiautomator1'

x1, y1 = 6, 463
x2, y2 = 280, 463

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

TouchAction(driver).press(x=x1, y=y1).wait(1000).move_to(x=x2, y=y2).release().perform()

time.sleep(3)
driver.quit()