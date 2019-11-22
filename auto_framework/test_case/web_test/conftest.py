import pytest
from test_case.web_test.pages import baidu_page
#web地址
web_url = 'https://www.baidu.com'
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium

@pytest.fixture
def BaiDu(selenium):
    selenium.get(web_url)
    return baidu_page.BaiDu(selenium)
