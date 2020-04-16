'''添加商品页面'''
from time import sleep


class AddGoodsPageGeneral(object):
	def __init__(self, driver):
		self.driver = driver
		self.driver.switch_to.frame("main_frame")
	goods_name = ("css selector", "input[name=goods_name]")
	goods_cate = ("css selector", "input#cat_name")
	goods_price = ("css selector", "input[name=shop_price]")
	submit = ("css selector", "input#goods_info_submit")

	def input_goods_name(self, text):
		self.driver.find_element(*self.goods_name).send_keys(text)

	def input_goods_cate(self, text):
		self.driver.find_element(*self.goods_cate).send_keys(text)

	def input_goods_price(self, text):
		self.driver.find_element(*self.goods_price).send_keys(text)

	def click_submit(self, ):
		self.driver.find_element(*self.submit).click()
