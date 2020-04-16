# 练习4
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://115.28.108.130/control.html')

driver.maximize_window()

driver.find_element_by_id('buttonID').click()
# 退出alert弹框
driver.switch_to.alert.accept()

driver.find_element_by_partial_link_text('在新页面').click()
# 切换到新窗口
all_win = driver.window_handles
driver.switch_to.window(all_win[1])
sleep(3)

driver.find_element_by_css_selector("div[id='u1']>a[class='lb']").click()
sleep(2)
driver.find_element_by_css_selector("p[title='用户名登录']").click()
# DOM弹框
driver.find_element_by_css_selector("input[name='userName']").send_keys("adb123")

# 授权框处理url中带上用户名&密码
# driver.get('http://***?username=""&password="" ')

sleep(5)
driver.quit()
