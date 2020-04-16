from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("http://115.28.108.130/control.html")

select_ele = Select(driver.find_element_by_id("areaID"))
select_ele.select_by_value('4')
sleep(2)
select_ele.select_by_visible_text('北京')
sleep(2)
select_ele.select_by_index('0') #角标从0开始
sleep(2)
driver.quit()