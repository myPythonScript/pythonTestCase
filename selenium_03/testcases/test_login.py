from time import sleep


class LoginPage(object):
    username_ipt_loc = ("css selector", "input[name='username']")
    password_ipt_loc = ("css selector", "input[name='password']")
    submit_btn_loc = ("class name", "button2")

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        print("用户名", username)
        username_input = self.driver.find_element(*self.username_ipt_loc)
        username_input.clear()
        username_input.send_keys(username)

    def input_password(self, password):
        print("密码", password)
        password_input = self.driver.find_element(*self.password_ipt_loc)
        password_input.clear()
        password_input.send_keys(password)

    def button_login(self):
        print("点击登录按钮")
        login_button = self.driver.find_element(*self.submit_btn_loc)
        login_button.click()

    def login(self, user, pwd):
        self.input_username(user)
        self.input_password(pwd)
        self.button_login()
        sleep(2)


def test_login(selenium):
    selenium.get("http://39.104.14.232/newecshop/admin/privilege.php?act=login")
    lp = LoginPage(selenium)
    lp.input_username("admin")
    lp.input_password("123456")
    lp.button_login()
    sleep(5)
    assert "frame-all" in selenium.page_source
