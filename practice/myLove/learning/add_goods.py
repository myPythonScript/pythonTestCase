from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest

class add_goods(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login")
		self.driver.maximize_window()
	def tearDown(self):
		self.driver.quit()

	def login(self,name,passw):
		username = self.driver.find_element_by_name("username")
		username.clear()
		username.send_keys(name)
		password = self.driver.find_element_by_name("password")
		password.clear()
		password.send_keys(passw)
		self.driver.find_element_by_class_name("button2").click()
	def test_add_class(self):
		self.login("super", "w123456")
		sleep(10)
		all_win = self.driver.window_handles
		new_win = self.driver.current_window_handle
		if new_win in all_win:
			#跳到新的窗口
			self.driver.switch_to.window(new_win)
			# print(driver.current_url)
			# 跳到frame中
			self.driver.switch_to.frame("menu-frame")
			#点击商品管理
			menu = self.driver.find_elements_by_class_name("button")
			menu[0].click()
			sleep(5)
			#点击商品分类
			self.driver.find_element_by_xpath('//*[@id="02_cat_and_goods"]/ul/li[4]/a').click()
			sleep(5)
			self.driver.switch_to.parent_frame()
			self.driver.switch_to.frame("main-frame")
			#点击添加分类
			self.driver.find_element_by_class_name("action-span").click()
			sleep(5)
			#输入分类名称
			self.driver.find_element_by_name("cat_name").send_keys("li好吃的")
			# 输入录名称
			self.driver.find_element_by_name("path_name").send_keys("li食品")
			#选择上级分类
			# driver.find_element_by_name('parent_id').click()
			# sleep(2)
			self.driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[3]/td[2]/select/option[2]').click()
			#输入数量单位
			self.driver.find_element_by_name("measure_unit").send_keys("个")
			#排序
			order = self.driver.find_element_by_name("sort_order")
			order.clear()
			order.send_keys("1")
			#是否显示
			self.driver.find_elements_by_name("is_show")[0].click()
			#是否在导航栏显示
			self.driver.find_elements_by_name("show_in_nav")[1].click()
			#首页推荐
			self.driver.find_elements_by_name("cat_recommend[]")[0].click()
			#筛选属性
			self.driver.find_element_by_css_selector("#tbody-attr > tbody > tr > td > select:nth-child(2) > option:nth-child(2)").click()
			#价格区间
			grade = self.driver.find_element_by_name("grade")
			grade.clear()
			grade.send_keys("8")
			#分类的样式文件
			self.driver.find_element_by_name("style").send_keys("themes/style.css")
			#关键字
			self.driver.find_element_by_name("keywords").send_keys("吃")
			#分类描述
			self.driver.find_element_by_name("cat_desc").send_keys("好吃不贵，绝对价廉物美！")
			#提交
			self.driver.find_elements_by_class_name("button")[0].click()
			sleep(2)
			#断言
			res = self.driver.find_element_by_class_name("list-div")
			assert "成功" in res.text

	def test_add_goods(self):
		self.login("super", "w123456")
		sleep(10)
		all_win = self.driver.window_handles
		new_win = self.driver.current_window_handle
		if new_win in all_win:
			#跳到新的窗口
			self.driver.switch_to.window(new_win)
			self.driver.switch_to.frame("menu-frame")
			#点击商品管理
			menu = self.driver.find_elements_by_class_name("button")
			menu[0].click()
			sleep(5)
			#点击“添加新商品”
			self.driver.find_element_by_xpath('//*[@id="02_cat_and_goods"]/ul/li[3]/a').click()
			sleep(3)
			self.driver.switch_to.parent_frame()
			self.driver.switch_to.frame("main-frame")

			# #输入“商品名称”
			self.driver.find_element_by_name("goods_name").send_keys("li最爱巧克力")
			# 输入“商品货号”
			self.driver.find_element_by_name("goods_sn").send_keys("888888")
			#选择“商品分类”
			self.driver.find_element_by_name("cat_name").click()
			sleep(5)
			self.driver.find_element_by_id("treeDemo_cat_id_1_switch").click()
			self.driver.find_element_by_id("treeDemo_cat_id_2_span").click()
			# 选择“扩展分类”
			area = self.driver.find_element_by_name("other_cat[]")
			sele = Select(area)
			sele.select_by_value("666")
			#选择“商品品牌”
			self.driver.find_element_by_id('brand_search').click()
			self.driver.find_element_by_id('appleapple').click()
			#选择“供货商”
			self.driver.find_element_by_id("suppliers_id").click()
			sleep(1)
			self.driver.find_element_by_xpath('//*[@id="suppliers_id"]/option[3]').click()
			#“本店售价”
			price = self.driver.find_element_by_name("shop_price")
			price.clear()
			price.send_keys("10")
			#手机专享价
			iphone = self.driver.find_element_by_name("exclusive")
			iphone.clear()
			iphone.send_keys("-1")
			#会员价
			userPrice = self.driver.find_elements_by_name("user_price[]")
			for u_price in userPrice:
				u_price.clear()
				u_price.send_keys("-1")
			#优惠数量
			self.driver.find_element_by_name("volume_number[]").send_keys("5")
			#优惠价格
			self.driver.find_element_by_name("volume_price[]").send_keys("10")
			#市场售价
			mark_price = self.driver.find_element_by_name("market_price")
			mark_price.clear()
			mark_price.send_keys("199")
			#赠送消费积分数
			give_int = self.driver.find_element_by_name("give_integral")
			give_int.clear()
			give_int.send_keys("-1")
			#赠送等级积分数
			rank_int = self.driver.find_element_by_name("rank_integral")
			rank_int.clear()
			rank_int.send_keys("-1")
			#选择促销
			self.driver.find_element_by_id("is_promote").click()
			# 促销价格
			pro_price = self.driver.find_element_by_name("promote_price")
			pro_price.clear()
			pro_price.send_keys("158")
			#限购数量
			self.driver.find_element_by_name("is_buy").click()
			sleep(1)
			self.driver.find_element_by_name("buymax").send_keys("3")
			#限购日期
			self.driver.find_element_by_name("selbtn3").click()
			cal = self.driver.find_elements_by_class_name("calendar")[0]
			srow = cal.find_elements_by_class_name("daysrow")[3]
			elem = srow.find_elements_by_class_name("day")[3]
			ActionChains(self.driver).double_click(elem).perform()

			self.driver.find_element_by_name("selbtn4").click()
			end_cal = self.driver.find_elements_by_class_name("calendar")[1]
			end_srow = end_cal.find_elements_by_class_name("daysrow")[4]
			end_elem = end_srow.find_elements_by_class_name("day")[4]
			ActionChains(self.driver).double_click(end_elem).perform()
			#分成金额
			cost_price = self.driver.find_element_by_name("cost_price")
			cost_price.clear()
			cost_price.send_keys("5")
			#上传图片
			self.driver.find_element_by_name("goods_img").send_keys("D:\Documents\Downloads\9cb8d5bbde64e31df7c9d359851ca168.jpeg")
			sleep(7)
			#自动生成锁略图
			# self.driver.find_element_by_name("auto_thumb").click()
			#确认
			self.driver.find_element_by_id("goods_info_submit").click()
			sleep(2)
			# 断言
			res = self.driver.find_element_by_class_name("list-div")
			assert "成功" in res.text

	def test_search_goods(self):
		self.login("super", "w123456")
		sleep(10)
		all_win = self.driver.window_handles
		new_win = self.driver.current_window_handle
		if new_win in all_win:
			#跳到新的窗口
			self.driver.switch_to.window(new_win)
			self.driver.switch_to.frame("menu-frame")
			#点击商品管理
			menu = self.driver.find_elements_by_class_name("button")
			menu[0].click()
			sleep(5)
			#点击“添加新商品”
			self.driver.find_element_by_xpath('//*[@id="02_cat_and_goods"]/ul/li[1]/a').click()
			sleep(3)
			self.driver.switch_to.parent_frame()
			self.driver.switch_to.frame("main-frame")

			self.driver.find_element_by_name("keyword").send_keys("li最爱巧克力")
			self.driver.find_elements_by_class_name("button")[0].click()
			sleep(5)
			self.driver.save_screenshot("learning/search.png")


















