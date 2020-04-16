from time import sleep


class GoodSearch(object):

    search_ipt_loc = ("css selector", "input#cat_name")
    search_cate_loc = ("id", "treeDemo_cat_id_46_a")
    search_btn_loc = ("css selector", "input[type=submit]")

    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        self.driver.find_element(*self.search_ipt_loc).click()

    def search_cate_input(self):
        self.driver.find_element(*self.search_cate_loc).click()

    def search_button(self):
        self.driver.find_element(*self.search_btn_loc).click()

    def search(self):
        self.search_input()
        self.search_cate_input()
        self.search_button()
        sleep(3)