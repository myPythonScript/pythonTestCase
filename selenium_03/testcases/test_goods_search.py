from time import sleep

from pages.goods_login import GoodsLoginPage
from pages.goods_menu import GoodsMenuPage
from pages.goods_add import AddGoodsPageGeneral
from pages.goods_search import GoodSearch


# def test_login(selenium):
#     selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
#     login_page = LoginPage(selenium)
#     login_page.login("admin", "123456")
#     assert "成功" in login_page.driver.page_source


def test_goods_search(selenium):
    # 1.登录
    selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
    login_page = GoodsLoginPage(selenium)
    login_page.login("admin", "123456")

    # ２.点击菜单
    menu_page = GoodsMenuPage(selenium)
    menu_page.click_menu("商品管理")
    menu_page.click_submenu("添加新商品")

    # 3.添加商品
    add_goods_page = AddGoodsPageGeneral(selenium)
    add_goods_page.input_goods_name("iphone10 pro")
    add_goods_page.input_goods_cate("手机、数码、通信")
    add_goods_page.input_goods_price("12000")
    add_goods_page.click_submit()
    sleep(2)

    # ２.点击菜单
    menu_page.click_submenu("商品列表")
    sleep(2)

    # 4.查找商品
    goods_search = GoodSearch(selenium)
    goods_search.search_input()
    goods_search.search_cate_input()
    goods_search.search_button()
    sleep(5)
    assert "iphone10 pro" in selenium.page_source


