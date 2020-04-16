'''菜单页面'''
from time import sleep


class GoodsMenuPage(object):
	def __init__(self, driver):
		self.driver = driver

	def click_menu(self, menu):
		print("点击菜单", menu)
		self.driver.switch_to.frame("menu_frame")
		self.driver.find_element("link text", menu).click()
		sleep(0.5)

	def click_submenu(self, sub_menu):
		print("选择菜单", sub_menu)
		self.driver.find_element("link text", sub_menu).click()
		self.driver.switch_to.default_content()
		sleep(10)