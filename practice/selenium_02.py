from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://39.104.14.232/ecshop/wwwroot/')

driver.maximize_window()

driver.find_element_by_id('keyword').send_keys("笔记本")
driver.find_element_by_class_name('main-bg-color').click()
driver.find_element_by_css_selector("div[class='item-pic']>a[href = 'goods.php?id=202']").click()

all_windowns = driver.window_handles
driver.switch_to.window(all_windowns[1])
sleep(3)

driver.find_element_by_link_text('加入购物车').click()
driver.find_element_by_class_name("span").click()

driver.switch_to.frame('formCart')
driver.find_element_by_link_text('去购物车结算').click()

all_windowns2 = driver.window_handles
driver.switch_to.window(all_windowns2[2])
sleep(3)

driver.find_element_by_class_name("jmcheckout").click()
driver.find_element_by_id("username").send_keys('admin')
driver.find_element_by_id("password").send_keys('123456')
driver.find_element_by_id("loginsubmit").click()

driver.quit()
