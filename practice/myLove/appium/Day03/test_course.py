from selenium import webdriver


class TestCourse(object):
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.quit()

    def login(self):
        print("登录")
        self.driver.get('http://qaschool.cn:8000/admin/')
        self.driver.find_element_by_id('id_username').send_keys('hanzhichao')
        self.driver.find_element_by_id('id_password').send_keys('hanzhichao123')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()

    def test_add_subject(self):
        self.login()
        self.driver.find_element_by_xpath('//a[text()="Subjects"]/../../td/a').click()
        self.driver.find_element_by_id('id_title').send_keys('GoLang')
        self.driver.find_element_by_name('_save').click()
        assert self.driver.find_elements_by_link_text('GoLang')

    def test_view_subject(self):
        self.login()
        self.driver.find_element_by_link_text('Subjects').click()
        assert self.driver.find_elements_by_link_text('性能测试')





