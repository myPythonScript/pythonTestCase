from time import sleep
import os

import pytest

from pages.baidu import BaiduPage
from utils.data import load_csv

basedir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'data', 'baiduSearch.csv')
data = load_csv(file_path)


@pytest.mark.parametrize("text", data)
def test_baidu_search(selenium, text):
    selenium.get("https://www.baidu.com")
    baidu = BaiduPage(selenium)
    text = text[0]
    baidu.search(text)
    sleep(3)
    assert text in selenium.title
