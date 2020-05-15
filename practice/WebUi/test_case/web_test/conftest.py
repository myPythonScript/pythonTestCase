import pytest
from test_case.web_test.pages.baidu_page import BaiduPage
from test_case.web_test.pages.login_page import LoginPage
from test_case.web_test.pages.menu_page import MenuPage
from test_case.web_test.pages.add_goods_page import AddGoodsPage
from test_case.web_test.pages.goods_list_page import GoodsListPage
from datetime import datetime
import os

@pytest.fixture
def selenium(selenium):
	selenium.implicitly_wait(10)
	# selenium.maxmize_window()
	return selenium

@pytest.fixture
def chrome_options(chrome_options):
	chrome_options.add_argument('--start-maximize')
	#不弹出界面运行
	# chrome_options.add_argument('--headless')
	return chrome_options

@pytest.fixture
def baidu_page(selenium):
	selenium.get('http://www.baidu.com')
	page = BaiduPage(selenium)
	return page
@pytest.fixture
def login_page(selenium):
	#1.进入这个页面
	selenium.get('http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login')
	#2.生成并返回页面对像
	return LoginPage(selenium)

@pytest.fixture
def menu_page(selenium,login_page):
	#1.进入这个页面
	login_page.login('admin','123456')
	#2.生成并返回页面对像
	return MenuPage(selenium)

@pytest.fixture
def add_goods_page():
	#1.进入这个页面
	menu_page.click_menu('商品管理','添加商品')
	#2.把页面对像返回给用例
	return AddGoodsPage(selenium)

@pytest.fixture
def goods_list_page():
	#1.进入这个页面
	menu_page.click_menu('商品管理', '商品列表')
	#2.把页面对像返回
	return GoodsListPage(selenium)

def pytest_configure(config):
	# print('------------------')
	# 	# print("给我买瓶水")
	# 	# #print(dir(config))
	# 	# #print(config.__dict__)
	# report = config.getoption("htmlpath")
	if config.getoption("htmlpath"):
		now = datetime.now().strftime("%Y%m%d_%H%M%s")
		# print(report)
		config.option.htmlpaty = os.path.join(config.rootdir,'reports',f'WEB_report_{now}.html')