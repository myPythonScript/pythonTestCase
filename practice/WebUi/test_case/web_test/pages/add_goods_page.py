class AddGoodsPage(object):
	goods_name_ipt_loc=('name','goods_name')
	category_name_ipt_loc=('id','category_name')
	price_ipt_loc=('name','shop_prince')
	submint_btn_loc=('id','goods_info_submit')
	def __init__(self,driver):
		self.driver = driver
		self.dirver.switch_to.frame('main-frame')
	def add_goods_page(self,goods_name):
		self.driver.find_element(*self.goods_name_ipt_loc).send_keys(goods_name)
	def input_category(self,category_name):
		self.driver.find_element(*self.category_name_ipt_loc).send_keys(category_name)
	def input_price(self,price):
		self.driver.find_element(*self.price_ipt_loc).senk_keys(price)

	def sumbit(self):
		self.driver.find_element(*self.submint_btn_loc).clice()