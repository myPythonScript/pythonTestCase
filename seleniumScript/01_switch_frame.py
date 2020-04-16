from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://115.28.108.130/control.html")

driver.maximize_window()

driver.switch_to.frame("parent_frame") #id,name等都可以定位
driver.switch_to.frame("left")
driver.find_element_by_link_text("链接2").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("top")
driver.find_element_by_link_text("百度").click()

sleep(5)
driver.quit()
