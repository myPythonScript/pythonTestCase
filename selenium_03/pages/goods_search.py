from time import sleep


class GoodSearch(object):

    search_keyword_loc = ("css selector", "input[name=keyword]")
    search_btn_loc = ("css selector", "input[type=submit]")

    def __init__(self, driver):
        self.driver = driver

    def search_keyword_input(self, keyword):
        kwd_input = self.driver.find_element(*self.search_keyword_loc)
        kwd_input.clear()
        kwd_input.send_keys(keyword)

    def search_button(self):
        self.driver.find_element(*self.search_btn_loc).click()

    def search(self):
        self.search_keyword_input()
        self.search_button()