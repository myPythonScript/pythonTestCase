# encoding = utf-8
import pytest
from time import sleep


class BaiDu(object):
    search_ipt_loc = ("id", "kw")
    search_btn_loc = ("id", "su")

    def __init__(self, driver):
        self.driver = driver

    def input_keyword(self, text):
        search_ipt = self.driver.find_element(*self.search_ipt_loc)
        search_ipt.clear()
        search_ipt.send_keys(text)

    def click_btn(self):
        search_btn = self.driver.find_element(*self.search_btn_loc)
        search_btn.click()

    def search(self, text):
        self.input_keyword(text)
        self.click_btn()


data = ["selenium", "抗击疫情", "五一假"]


@pytest.mark.parametrize("keyword", data)
def test_search(selenium, keyword):
    selenium.get("https://www.baidu.com/")
    bd = BaiDu(selenium)
    bd.search(keyword)
    sleep(2)
    assert keyword in selenium.title
