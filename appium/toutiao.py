from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62025",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "automationName": "uiautomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(15)

# open_ele = driver.find_elements_by_accessibility_id("com.ss.android.article.lite:id/a80")
# if len(open_ele) != 0:
#     driver.tap([("750","1800")])
#
# else:
#     print("倒计时中...")



