from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    print("启动浏览器")
    driver = webdriver.Chrome()
    yield driver
    print("退出浏览器")
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get('http://qaschool.cn:8000/admin/')
    driver.find_element_by_id('id_username').send_keys('hanzhichao')
    driver.find_element_by_id('id_password').send_keys('hanzhichao123')
    driver.find_element_by_xpath('//input[@type="submit"]').click()


class TestCourse(object):
    def test_add_subject(self, driver, login):
        print("添加subject")
        driver.find_element_by_xpath('//a[text()="Subjects"]/../../td/a').click()
        driver.find_element_by_id('id_title').send_keys('GoLang22')
        driver.find_element_by_name('_save').click()
        assert driver.find_elements_by_link_text('GoLang22')

    def test_view_subject(self, driver, login):
        print("查看subject")

        driver.find_element_by_link_text('Subjects').click()
        assert driver.find_elements_by_link_text('性能测试')
