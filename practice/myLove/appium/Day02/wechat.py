from appium import webdriver
from time import sleep

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
	"appPackage": "cn.kmob.screenfingermovelock",
	"appActivity": "com.samsung.ui.FlashActivity",
	"autoLaunch":False
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.launch_app("com.lqr.wechat")
driver.press_keycode(4)

# 打开通知栏
driver.open_notifications()
sleep(2)
driver.press_keycode(4)

# 启动浏览器
driver.start_activity("com.android.browser","com.android.browser.BrowserActivity")
sleep(3)
activity = driver.current_activity
if (".BrowserActivity" == activity):
	print("当前activity正确")
else:
	print("activity不正确")



#截图
driver.save_screenshot("f:\截图.png")

#查看当前网络
network = driver.network_connection
print(network)

#放在后台运行
driver.background_app("5")
driver.press_keycode(4)
sleep(2)
#判断微信是否以安装
installed  = driver.is_app_installed('com.lqr.wechat')
if installed:
	print("已安装")
	driver.remove_app("com.lqr.wechat")
else:
	print("未安装")
	driver.install_app("F:/appium/app-debug/app-debug.apk")