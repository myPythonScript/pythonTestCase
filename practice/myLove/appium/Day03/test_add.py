import requests
import pytest

def test_1():
	res = requests.get("http://115.28.108.130:5000/add/?a=1&b=2")
	print(res.text)
	assert res.text == '3'

def test_2():
	res = requests.get("http://115.28.108.130:5000/add/?a=2&b=4")
	print(res.text)
	assert res.text == '6'

def test_3():
	res = requests.get("http://115.28.108.130:5000/add/?a=2&b=9")
	print(res.text)
	assert res.text == '11'

if __name__ == "__main__":
	pytest.main(["test_add.py","-qs"])