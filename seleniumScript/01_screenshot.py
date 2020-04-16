from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_link_text("新闻").click()
sleep(5)

driver.save_screenshot("C:/Users/Administrator/Desktop/新闻.png")

print(driver.title)
if driver.title == '百度新闻——海量中文资讯平台':
    print("打开百度新闻成功")

if "海量中文资讯平台" in driver.page_source:
    print("新闻打开成功")

driver.quit()
