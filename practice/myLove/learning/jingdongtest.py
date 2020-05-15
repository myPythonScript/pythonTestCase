from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://39.104.14.232/ecshop/wwwroot/")
driver.maximize_window()

def test_earch():
    driver.find_element_by_name('keywords').send_keys("水果")
    driver.find_element_by_xpath('//input[@type="submit" and @value="搜索"]').click()
    driver.find_element_by_css_selector('li[id="li_229"]').click()
    all_win = driver.window_handles
    search_win = driver.current_window_handle
    #切换到新窗口
    for new_win in all_win:
        if (new_win != search_win):
            driver.switch_to.window(new_win)
            sleep(10)
            js = '''var q = document.documentElement.scrollTop=1000;     
            '''
            driver.execute_script(js)

            #点击加入购物车
            driver.find_element_by_class_name('u-buy2').click()
            sleep(15)
            #点击界面右上角的购物车
            driver.find_element_by_css_selector('a[id="mc-menu-hd"]').click()
            sleep(20)
            #去结算
            driver.find_element_by_xpath('//a[@class="jmcheckout"]').click()
            sleep(20)
            #登录
            driver.find_element_by_css_selector('input[id="username"]').send_keys("admin")
            driver.find_element_by_css_selector('input[id="password"]').send_keys("123456")
            driver.find_element_by_css_selector('input[id="loginsubmit"]').click()
            sleep(10)
            driver.find_element_by_xpath('//a[@class="jmcheckout"]').click()
            sleep(5)
            driver.find_element_by_css_selector('div[class="address_jm_add"]').click()
            #新加地址
            driver.switch_to.alert
            driver.find_element_by_css_selector('input[name="consignee"]').send_keys('韦丽丽')
            driver.find_element_by_xpath('//div[@id="PopAddressCon"]/table/tbody/tr[2]/td[2]/select[1]').click()
            driver.find_element_by_xpath('//div[@id="PopAddressCon"]/table/tbody/tr[2]/td[2]/select[1]/option[24]').click()
            driver.find_element_by_xpath('//div[@id="PopAddressCon"]/table/tbody/tr[2]/td[2]/select[2]').click()
            driver.find_element_by_xpath('//div[@id="PopAddressCon"]/table/tbody/tr[2]/td[2]/select[2]/option[2]').click()
            driver.find_element_by_xpath('//input[ @name="address"]').send_keys('五路45号')
            driver.find_element_by_xpath('//input[ @name="email"]').send_keys('540224203@qq.com')
            driver.find_element_by_xpath('//input[ @name="zipcode"]').send_keys('710000')
            driver.find_element_by_xpath('//input[ @name="mobile"]').send_keys('13572500000')
            driver.find_element_by_xpath('//input[ @class="BonusButton" and @value=" 确定 "]').click()
            #送货时间
            driver.find_element_by_css_selector('input[id="time_delivery3"]').click()
            driver.find_element_by_xpath('//input[@value="6"]').click()
            driver.find_element_by_xpath('//input[@type="image"]').click()
            sleep(10)

