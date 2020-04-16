from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://39.104.14.232/ecshop/wwwroot/')

# 窗口最大化
driver.maximize_window()

# 搜索商品并加入购物车
driver.find_element_by_id('keyword').send_keys("笔记本")
driver.find_element_by_class_name('main-bg-color').click()
driver.find_element_by_css_selector("div[class='item-pic']>a[href = 'goods.php?id=202']").click()

all_windowns = driver.window_handles
driver.switch_to.window(all_windowns[1])
sleep(5)

driver.find_element_by_link_text('加入购物车').click()
driver.find_element_by_class_name("span").click()

# presence_of_element_located不关心元素是否可见，只关心元素是否存在在页面中
WebDriverWait(driver, 30).until(presence_of_element_located(('link text', "去购物车结算")))
driver.find_element_by_link_text("去购物车结算").click()

all_windowns2 = driver.window_handles
driver.switch_to.window(all_windowns2[2])
sleep(3)

# 点击去结算
driver.find_element_by_class_name("jmcheckout").click()
# 登录
driver.find_element_by_id("username").send_keys('admin')
driver.find_element_by_id("password").send_keys('123456')
driver.find_element_by_id("loginsubmit").click()
sleep(2)

# 点击去结算
driver.find_element_by_class_name("jmcheckout").click()
driver.find_element_by_css_selector("#AddressList>ul>li:nth-child(3)").click()
sleep(3)
# 拖动滚动条到可见的元素
target = driver.find_element_by_css_selector("input[type='image']")
driver.execute_script("arguments[0].scrollIntoView();", target)

js1 = '''
document.querySelector("div[class='checkBox_jm']>ul>li:nth-child(2)>input").removeAttribute('disabled');
'''
driver.execute_script(js1)
sleep(1)

# 货到付款
driver.find_element_by_css_selector("div[class='checkBox_jm']>ul>li:nth-child(2)>input").click()
target.click()
get_order = (By.LINK_TEXT, "进入我的订单中心")
# visibility_of_element_located需要找到元素，并且该元素也可见
WebDriverWait(driver, 50, 1).until(EC.visibility_of_element_located(get_order))

driver.quit()
