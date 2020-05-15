def login():
    driver = webdriver.Chrome()
    print("登录")
    driver.get('http://qaschool.cn:8000/admin/')
    driver.find_element_by_id('id_username').send_keys('hanzhichao')
    driver.find_element_by_id('id_password').send_keys('hanzhichao123')
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    return driver

def test_add_subject():
    driver = login()
    driver.find_element_by_xpath('//a[text()="Subjects"]/../../td/a').click()
    driver.find_element_by_id('id_title').send_keys('GoLang')
    driver.find_element_by_name('_save').click()
    assert driver.find_elements_by_link_text('GoLang')

def test_view_subject():
    driver = login()
    driver.find_element_by_link_text('Subjects').click()
    assert driver.find_elements_by_link_text('性能测试')
