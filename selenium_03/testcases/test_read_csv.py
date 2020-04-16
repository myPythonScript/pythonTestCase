import os
from time import sleep
import pytest

# 组装文件路径,1.根据当前文件路径计算出项目根路径
# 当前文件：__file__
# os.path.dirname(__file__)相当于testcases
basedir = os.path.dirname(os.path.dirname(__file__))
# 2.组装文件数据路径
file_path = os.path.join(basedir, 'data', 'baiduSearch.csv')
data = load_csv()

class baiduPage(object):
	search_ipt_loc = ("id", "kw")
	search_btn_loc = ("id", "su")

	def __init__(self, driver):
		self.driver = driver

	def input_keyword(self, text):
		search_input = self.driver.find_element(*self.search_ipt_loc)
		search_input.clear()
		search_input.send_keys(text)

	def click_btn(self):
		self.driver.find_element(*self.search_btn_loc).click()

	def search(self, text):
		self.input_keyword(text)
		self.click_btn()


# def test_baidu_search(selenium):
# 	selenium.get("https://www.baidu.com")
# 	baidu = baiduPage(selenium)
# 	baidu.search("selenium")
# 	sleep(3)
# 	assert "selenium" in selenium.page_source

data = ['selenium', '樱花', '美国']
@pytest.mark.parametrize('keyword', data)
def test_baidu_search(selenium, keyword):
	selenium.get("https://www.baidu.com")
	baidu = baiduPage(selenium)
	baidu.search(keyword)
	sleep(2)
	assert keyword in selenium.title

