from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://115.28.108.130/control.html")

driver.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\Administrator\\Desktop\\123.txt")
sleep(2)
driver.quit()
driver.window_handles