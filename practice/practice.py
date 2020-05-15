# 练习6
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get('http://115.28.108.130/control.html')
# input_ele = driver.find_element_by_id('check')
# input_ele.send_keys('中巴友谊')
# sleep(2)
# input_ele.send_keys(Keys.CONTROL, 'a')
# sleep(2)
# input_ele.send_keys(Keys.CONTROL, 'c')
# sleep(2)
# input_ele.clear()
#
# driver.find_element_by_link_text('在新页面打开百度').click()
#
# all_win = driver.window_handles
#
#
# driver.switch_to.window(all_win[1])
# sleep(2)
#
# seache_ele = driver.find_element_by_id('kw')
# seache_ele.send_keys(Keys.CONTROL, 'V')
#
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.quit()

# 练习7
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# select_ele = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(select_ele).perform()
#
# select_ele = driver.find_element_by_link_text('高级搜索').click()
# sleep(2)
#
# driver.quit()

# # 练习9
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get('http://115.28.108.130/date.html')
#
# js = '''
# 	document.querySelector("input[name='act_start_time']").removeAttribute('readonly');
# '''
#
# driver.execute(js)
# driver.find_element_by_name('act_start_time').send_keys('2020-4-4 16:40')
# driver.fin
#
# sleep(5)
# driver.quit()


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://39.104.14.232/ecshop/wwwroot/goods.php?id=202')

driver.maximize_window()

driver.find_element_by_link_text('加入购物车').click()
driver.find_element_by_class_name("span").click()
driver.switch_to.frame('formCart')
driver.find_element_by_css_selector('#formCart > div > div.cart-panel-footer > div > a').click()

