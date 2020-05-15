from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction


caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = 'cn.kmob.screenfingermovelock'
caps['appActivity'] = 'com.samsung.ui.FlashActivity'
#　模拟器
caps['uiautomator'] = 'Uiautomator1'
# caps['uiautomator'] = 'Uiautomator2'  #真机

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.find_element_by_xpath("//*[@text='设置手势密码']").click()


