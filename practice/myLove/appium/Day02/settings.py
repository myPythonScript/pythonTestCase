from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

#获取屏幕分辩率
size = driver.get_window_size()
width = size['width']
height = size['height']
print(size)
#计算屏幕点击坐标
x1 = x2 = width/2
y1 = height * 0.9
y2 = height * 0.1

#慢滑，可以控制滑动时间，毫秒为单位
# driver.swipe(x1, y1, x2, y2, duration=1000)
results = driver.find_elements_by_xpath("//*[@text='关于平板电脑']")

#向上滑动之后，是否找到要找的元素
for i in range(5):
    if results:
        break
    # 快滑，不可控制滑动时间
    driver.flick(x1, y1, x2, y2)
    results = driver.find_elements_by_xpath("//*[@text='关于平板电脑']")

#找到元素后，点击
if results:
    results[0].click()
