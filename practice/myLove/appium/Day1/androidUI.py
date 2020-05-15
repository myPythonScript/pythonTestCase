from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.android.androidui"
caps["appActivity"] = "com.android.androidui.MainActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("com.android.androidui:id/mySwitch").click()
driver.find_element_by_id("com.android.androidui:id/buttonAlert").click()
driver.find_element_by_id("android:id/button1").click()

driver.quit()
