'''菜单页面'''
from time import sleep

class MenuPage(object):
	def __init__(self, driver):
		self.driver = driver

	def click_menu(self, menu, sub_menu):
		print("点击菜单", menu, sub_menu)
		self.driver.switch_to.frame("menu_frame")
		self.driver.find_element("link text", menu).click()
		sleep(0.5)
		self.driver.find_element("link text", sub_menu).click()
		self.driver.switch_to.default_content()
		sleep(10)