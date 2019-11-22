from time import sleep

class BaiDu(object):
    search_inp_loc = ('id','kw')
    search_btn_loc = ('id','su')
    def __init__(self,driver):
        self.driver = driver
    def send_baidu_search_input(self):
        self.driver.find_element(*self.search_inp_loc).send_keys('selenium')
    def send_baidu_search_button(self):
        self.driver.find_element(*self.search_btn_loc).click()
    def search(self):
        self.send_baidu_search_input()
        sleep(1)
        self.send_baidu_search_button()
        sleep(2)
