# 1. 从appium导入webdriver
from appium import webdriver
import time


# 2. 启动项配置
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['app'] = r'D:\15期\Appium\day01\app-debug.apk'
# caps['autoLaunch'] = False  # 不自动启动app


# 3. 连接appium服务
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# 4. 操作app
is_installed = driver.is_app_installed('com.lqr.wechat')
print('是否已安装', is_installed)
if is_installed is True:  # 如果已安装
    # driver.launch_app()  # 手动启动app
    print('已安装')

# 登录
driver.find_element('xpath', '//*[@text="登录"]').click()

elements = driver.find_elements('class name', 'android.widget.EditText')
elements[0].send_keys('18010181267')
elements[1].send_keys('123456')
driver.find_element('xpath', '//*[@text="登录"]').click()
time.sleep(5)

# 右滑driver.swipe(x1,y1,x2,y2)
size = driver.get_window_size()
print('屏幕尺寸', size)
width = size['width']
height = size['height']

x1,y1,x2,y2 = width*0.9, height/2, width*0.1, height/2


print('滑动屏幕')
driver.swipe(x1,y1,x2,y2, duration = 2000)
time.sleep(1)
driver.save_screenshot('D:\\weixin.png')
# driver.keyevent(3)  # 按Home键


time.sleep(3)
driver.quit()