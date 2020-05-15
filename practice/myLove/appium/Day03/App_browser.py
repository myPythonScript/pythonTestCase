from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "browserName":"Chrome"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.get("http://baidu.com")
driver.find_element_by_id("")