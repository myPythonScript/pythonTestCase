from appium import webdriver
from time import sleep

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.example.testapp",
    "appActivity": "com.example.testapp.MainActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element_by_id("com.example.testapp:id/urlField").send_keys("http://m.baidu.com")
driver.find_element_by_id("com.example.testapp:id/goButton").click()

sleep(3)
print(driver.context)

driver.switch_to.context('WEBVIEW_com.example.testapp')

print(driver.context)

driver.find_element_by_id("index-kw").send_keys("Appium")
driver.find_element_by_id("index-bn").click()

driver.switch_to.context('NATIVE_APP')