class MenuPage(object):
	def __init__(self,driver):
		self.driver = driver
		self.click_menu.switch_to.frame('menu_frame')
	def click_menu(self,menu_name,sub_menu_name):
		menu_name = '商品管理'
		sub_menu_name = '添加新商品'
		self.driver.find_element_by_link_text('商品管理').clic()
		self.driver.find_element_by_link_text('添加新商品').clic()

		self.driver.switch_to.default_content()
