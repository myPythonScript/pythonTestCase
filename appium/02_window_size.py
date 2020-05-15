from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = 'com.android.settings'
caps['appActivity'] = '.Settings'


driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
size = driver.get_window_size()
height = size['height']
width = size['width']
x1, y1, x2, y2 = width/2, height*0.9, width/2, height*0.1

def swipe_up_and_find(driver):
    # driver.swipe(x1, y1, x2, y2,duration=1)
    driver.flick(x1,y1,x2,y2)
    return driver.find_element('xpath', '//*[@text="关于平板电脑"]')  # 点击关于平板电脑


# 循环上滑和查找
WebDriverWait(driver, 30, 1).until(swipe_up_and_find).click()

# sleep(1)
# driver.swipe(x1, y1, x2, y2)
sleep(3)
driver.find_element_by_xpath("//*[@text='关于平板电脑']").click()
sleep(2)
ele = driver.find_element_by_xpath("//*[@text='Android版本']")
for i in range(7):
	ele.click()

sleep(4)
driver.quit()
