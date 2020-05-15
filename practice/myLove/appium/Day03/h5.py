from appium import webdriver
from time import sleep
caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.example.testapp',
    'appActivity': '.MainActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element_by_id('com.example.testapp:id/urlField').send_keys("http://m.baidu.com")
driver.find_element_by_id('com.example.testapp:id/goButton').click()

# 1. 如果通过appium inspector能识别并计算出页面元素基于原始APP上下文的XPath,不同切换上下文。
# sleep(2)
# driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="百度一下"]/android.widget.EditText').send_keys('Apppium')
# sleep(2)
# driver.find_element_by_xpath('//android.widget.Button[@content-desc="百度一下"]').click()

# 2. 如果appium inspector解析不出页面元素
# 切换上下文到webview,使用PC chrome浏览器的chrome://inspect审查远程设备
# 需要满足以下条件：
# 2.1 必须是debug包
# 2.2 手机上必须安装Chrome浏览器，本地有相应版本的chromedriver
# 2.3 手机上必须安装Google应用框架
# 2.4 需要翻墙

print(driver.contexts)  # 所有的上下文
# print(driver.context)  # 当前的上下文

# 默认上下文名为NATIVE_APP, 页面的上下文名一般是WEBVIEW_****
driver.switch_to.context("WEBVIEW_com.example.testapp")

driver.find_element_by_id('index-kw').send_keys('Appium')
driver.find_element_by_id('index-bn').click()




