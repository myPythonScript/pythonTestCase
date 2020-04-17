from time import sleep

from pages.goods_login import GoodsLoginPage
from pages.goods_menu import GoodsMenuPage
from pages.goods_add import AddGoodsPageGeneral
from pages.goods_search import GoodSearch


def test_goods_search(selenium):
    # 1.登录
    selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
    selenium.maximize_window()
    login_page = GoodsLoginPage(selenium)
    login_page.login("admin", "123456")

    # ２.点击菜单
    menu_page = GoodsMenuPage(selenium)
    menu_page.click_menu("商品管理")
    menu_page.click_submenu("添加新商品")

    # 3.添加商品
    keyword = "iphone10 pro"
    add_goods_page = AddGoodsPageGeneral(selenium)
    add_goods_page.input_goods_name(keyword)
    add_goods_page.input_goods_cate("手机、数码、通信")
    add_goods_page.input_goods_price("12000")
    add_goods_page.click_submit()
    selenium.implicitly_wait(20)

    # 5.查找商品
    print("查找商品")
    goods_search = GoodSearch(selenium)
    goods_search.search_keyword_input(keyword)
    goods_search.search_button()
    sleep(5)
    assert "iphone10 pro" in selenium.page_source
