from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://115.28.108.130/control.html")
sleep(2)

# 1.移动到指定位置
# js = """
# document.documentElement.scrollTop=10000
# """
# driver.execute_script(js)

# # 2.使用键盘下键操作
# driver.find_element_by_link_text("友情链接").send_keys(Keys.DOWN)

# 3.移动到某个元素所在位置
target = driver.find_element_by_link_text("友情链接")
driver.execute_script("arguments[0].scrollIntoView();", target)

sleep(5)
driver.quit()
