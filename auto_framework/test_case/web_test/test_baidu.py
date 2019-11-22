import pytest


@pytest.mark.web
def test_baidu_search(BaiDu):
    BaiDu.search()
