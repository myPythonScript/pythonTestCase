import time


class BaiduPage(object):
    def __init__(self, driver):
        self.driver = driver

    search_ipt_loc = ("id", "kw")
    search_btn_loc = ("id", "su")

    def search_input(self, text):
        search_ipt = self.driver.find_element(*self.search_ipt_loc)
        search_ipt.clear()
        search_ipt.send_keys(text)

    def search_button(self):
        search_btn = self.driver.find_element(*self.search_btn_loc)
        search_btn.click()

    def search(self, text):
        self.search_input(text)
        self.search_button()


def test_baidu_search(selenium):
    selenium.get("https://www.baidu.com/")
    time.sleep(2)

    baidu = BaiduPage(selenium)
    baidu.search("selenium")
    time.sleep(3)
    assert "selenium" in selenium.title
    selenium.quit()
