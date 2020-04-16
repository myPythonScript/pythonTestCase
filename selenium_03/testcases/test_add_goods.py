from pages.login import LoginPage
from pages.menu import MenuPage
from pages.add_goods import AddGoodsPageGeneral


def test_login(selenium):
	selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
	login_page = LoginPage(selenium)
	login_page.login("admin", "123456")
	assert "成功" in login_page.driver.page_source

def test_add_goods(selenium):
	# 1.登录
	selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
	login_page = LoginPage(selenium)
	login_page.login("admin", "123456")

	# ２.点击菜单
	menu_page = MenuPage(selenium)
	menu_page.click_menu("商品管理", "添加新商品")

	# 3.添加商品
	add_goods_page = AddGoodsPageGeneral(selenium)
	add_goods_page.input_goods_name("dell电脑")
	add_goods_page.input_goods_cate("电脑")
	add_goods_page.input_goods_price("4000")
	add_goods_page.click_submit()
	assert "添加成功" in selenium.page_source
