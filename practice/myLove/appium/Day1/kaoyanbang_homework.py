from appium import webdriver
from time import sleep

caps = {
	"platformName":"Android",
	"platformVersion": "5.1.1",
	"deviceName":"127.0.0.1:62001",
	"appPackage":"com.tal.kaoyan",
	"appActivity":"com.tal.kaoyan.ui.activity.SplashActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)

# 跳过按钮
try:
	em１ = driver.find_element_by_class_name('android.widget.TextView')
	em１.click()
except:
	pass
#取消更新按钮
try:
	em２ = driver.find_element_by_id("android:id/button2")
	em２.click()
except:
	pass
try:
	em３ = driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')
	em３.click()
except:
	pass

driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("superhin")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("hanzhichao")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

sleep(5)

driver.quit()