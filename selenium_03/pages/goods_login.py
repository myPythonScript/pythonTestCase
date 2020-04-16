'''登录页面'''
from time import sleep


class GoodsLoginPage(object):
	def __init__(self, driver):
		self.driver = driver

	username = ("name", "username")
	password = ("name", "password")
	button = ("class name", "button2")

	def input_username(self, user):
		print("输入用户名", user)
		self.driver.find_element(*self.username).send_keys(user)

	def input_password(self, pwd):
		print("输入密码", pwd)
		self.driver.find_element(*self.password).send_keys(pwd)

	def click_login(self):
		print("点击登录按钮")
		self.driver.find_element(*self.button).click()

	def login(self, user, pwd):
		self.input_username(user)
		self.input_password(pwd)
		self.click_login()
		sleep(2)