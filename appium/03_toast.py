from appium import webdriver
from time import sleep

caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = 'com.lqr.wechat'
caps['appActivity'] = '.ui.activity.SplashActivity'
caps['automationName'] = 'uiautomator2'

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element('xpath', '//*[@text="登录"]').click()
elms = driver.find_elements('class name', 'android.widget.EditText')
elms[0].send_keys('18010181267')
elms[1].send_keys('123')
driver.find_element('xpath', '//*[@text="登录"]').click()
sleep(0.2)
results = driver.find_elements('xpath', '//*[contains(@text,"登录失败")]')
if len(results) > 0:
    print('定位到了toast元素')
    print(results[0].text)
else:
    print('未定位到toast元素')
