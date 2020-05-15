import requests
import pytest
import PyYmal


def get_data():
    with open('data2.yaml') as f:
        data = PyYmal.safe_load(f)
    return data

# data = [[1,2,3],[0,2,2],[-1,2,1]]

@pytest.mark.parametrize('a,b,sum', get_data())
def test_add(a, b, sum):
    res = requests.get(f'http://115.28.108.130:5000/add/?a={a}&b={b}')
    assert res.text == f'{sum}'



# if __name__ == '__main__':
# 	pytest.main(['test_demo6.py','-qs'])




