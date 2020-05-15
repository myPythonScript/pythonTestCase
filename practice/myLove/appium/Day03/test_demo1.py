import requests
import pytest


def add():
    return 1+1

def test_1():
    print('执行test_1')
    assert 1+1 == 2


def test_2():
    print('执行test_2')
    res = requests.get('https://www.baidu.com')
    assert res.status_code == 200


if __name__ == '__main__':
    pytest.main(['test_demo1.py', '-qs'])
